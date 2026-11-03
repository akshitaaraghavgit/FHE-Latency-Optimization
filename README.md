# FHE-Latency-Optimization
A reproducible research project focused on benchmarking Fully Homomorphic Encryption (FHE), identifying CKKS performance bottlenecks, and exploring software and hardware optimizations to reduce computation latency.
# FHE Latency Optimization

## Overview

This project investigates performance bottlenecks in Fully Homomorphic Encryption (FHE), with an initial focus on the CKKS scheme.

The objective is to benchmark existing FHE implementations, identify computationally expensive operations, and investigate software and hardware-level optimizations to reduce execution latency.

## Objectives

- Establish a reproducible CPU baseline using OpenFHE.
- Benchmark individual CKKS operations.
- Investigate computational bottlenecks in polynomial arithmetic and modular operations.
- Evaluate potential optimizations.
- Explore hardware acceleration of selected computational kernels.
- Compare baseline and optimized performance.

## Technology Stack

- OpenFHE
- C/C++
- Linux
- CMake
- Python (benchmark analysis)
- Verilog (hardware implementation)

## Methodology

1. Benchmark existing FHE operations.
2. Record baseline performance.
3. Identify computational bottlenecks.
4. Investigate the underlying operations.
5. Implement selected optimizations.
6. Re-run benchmarks.
7. Compare performance and verify correctness.



- [ ] First optimization implemented.
- [ ] Performance comparison completed.
