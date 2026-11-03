# Baseline Benchmark Methodology

## Objective

Establish baseline performance measurements for three Fully Homomorphic Encryption (FHE) schemes: CKKS, BFV and BGV, using the existing benchmark suite provided by OpenFHE.

The purpose is to understand the computational costs of different homomorphic operations and establish a reference point for subsequent latency optimization.

## Benchmark Environment

- FHE library: OpenFHE
- Benchmark executable: `lib-benchmark`
- Benchmark framework: Google Benchmark
- Build configuration: Release
- Execution environment: Ubuntu Linux
- Thread configuration: `OMP_NUM_THREADS=1`
- Repetitions: 5

## Schemes Evaluated

### 1. CKKS
Supports approximate arithmetic on encrypted numerical data.

### 2. BFV
Supports exact integer arithmetic on encrypted data.

### 3. BGV
Supports exact modular arithmetic on encrypted data.

## Operations Evaluated

The available benchmark cases were inspected using OpenFHE's benchmark listing functionality.

The selected operation categories include:

- Key generation
- Encryption
- Decryption
- Homomorphic addition
- Homomorphic multiplication without relinearization
- Homomorphic multiplication with relinearization
- Relinearization, where available
- Ciphertext rotation
- Fast rotation
- Rescaling or modulus switching, where available

Multiplication benchmarks were examined at multiple depths: 1, 2, 4, 6, 8, 10 and 12.

## Measurement Procedure

OpenFHE's existing `lib-benchmark` executable was used to execute the available benchmark cases for each scheme.

Five repetitions were configured to assess measurement consistency.

Results were exported in JSON format for preservation and subsequent analysis.

## Measurement Metrics

- Mean execution time
- Median execution time
- Standard deviation
- Coefficient of variation (CV)
- Number of benchmark iterations

## Scope and Limitations

These measurements represent individual library-level benchmark operations. They do not, by themselves, establish end-to-end application latency or identify the dominant bottleneck in a complete FHE workload.

The three schemes support different computational models and operation sets. Comparisons must therefore account for differences in functionality and benchmark configuration.
