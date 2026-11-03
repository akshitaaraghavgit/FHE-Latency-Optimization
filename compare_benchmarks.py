import json
import csv
import re
from pathlib import Path

folder = Path.home() / "FHE-Latency-Optimization/results/baseline"

files = {
    "CKKS": ["ckks-operations.json", "ckks-mult-relin.json"],
    "BFV": ["bfv.json"],
    "BGV": ["bgv.json"]
}

rows = []

for scheme, filenames in files.items():
    for filename in filenames:
        with open(folder / filename) as f:
            data = json.load(f)

        for b in data.get("benchmarks", []):
            aggregate = b.get("aggregate_name")

            if aggregate not in ("mean", "median", "stddev", "cv"):
                continue

            name = b.get("name", "")
            name = re.sub(
                r"_(mean|median|stddev|cv)$", "", name
            )

            rows.append({
                "Scheme": scheme,
                "Benchmark": name,
                "Aggregate": aggregate,
                "RealTime": b.get("real_time", ""),
                "CPUTime": b.get("cpu_time", ""),
                "Unit": (
                    "ratio" if aggregate == "cv"
                    else b.get("time_unit", "")
                )
            })

output = folder / "combined-results.csv"

with open(output, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Scheme", "Benchmark", "Aggregate",
        "RealTime", "CPUTime", "Unit"
    ])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} records to {output}")
