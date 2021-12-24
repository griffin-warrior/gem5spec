# Run SPEC2017 Benchmark for POWER ISA Implementation in Gem5

## Test Environment

We only test SPEC base subset because currently gem5-power does not support running multithreaded programs.

Test passed under the environment descripted below:

Gem5 output from
- Arch: `x86_64`
- SPEC Compiler: `powerpc64le-linux-gnu-gcc/g++/gfortran` (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 (cross compiled on x86_64)
- OS: `Ubuntu 20.04.3 LTS`

Host output from
- Arch: `ppec64le`
- SPEC Compiler: `powerpc64le-linux-gnu-gcc/g++/gfortran` (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 (cross compiled on x86_64)
- OS: `Ubuntu 20.04.3 LTS`



##  Steps to Run Test

### Step 1: Compile SPEC2017

Compile `x86` and `ppc` respectively before running this test.
```bash
cp spec-config/*.cfg ${SPEC_HOEM}/config/
runcpu --action=build --config=x86 intrate fprate
runcpu --action=build --config=ppc intrate fprate
```

### Step 2: Config Script ENVs

Edit `runspec_gem5_power/Makefile.inc` according to your `SPEC_HOME` and gem5 repo path.

### Step 3: Run Host

Generate host results for comparison.

```bash
cd runspec_gem5_power/
make -j24 host LABEL=x86
```

### Step 4: Run Gem5

```bash
cd runspec_gem5_power/
make -j24 gem5
```

If gem5 crashed when running, the corresponding benchmark name will be recorded in `fail_gem5_crash.log`.

### Step 5: Diff Results

After gem5 test finished, check the results.
If there are failed benchmarks, they will be recorded in `fail_gem5_diff.log`.

```bash
cd runspec_gem5_power/
make diff
```



## Debug Benchmarks Separately

The steps above demonstrate how to run all of the 24 benchmarks together in parallel.

Running test can be very flexible. You can also go to a specific folder to run and debug a single benchmark. 

```bash
# Example
cd runspec_gem5_power/510.parest_r
make host LABEL=x86
make gem5 && make diff
```



## Known Issues

- Most host outputs are the same between x86 and power8 except for 508, 510, 527 with minor floating point precision discrepancy. We put these output files from power8 in `ref` folder.

- Output results of floating point precision may differ from binaries compiled by different compilers or the same compiler from different architectures.

