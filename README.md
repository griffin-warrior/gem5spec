# Run SPEC2017 Benchmark for POWER ISA Implementation in Gem5

## Test Environment

We only test SPEC base subset because currently gem5-power does not support running multithreaded programs.

Test passed under the environment descripted below:

Gem5 output from
- Arch: `x86_64`
- SPEC Compiler: `powerpc64le-linux-gnu-gcc/g++/gfortran` (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 (cross compiled on x86_64)
- SPEC Compiler: Advance Toolchain 15.0 on x86
- OS: `Ubuntu 20.04.3 LTS`

Host output from
- Arch: `ppec64le`
- SPEC Compiler: `powerpc64le-linux-gnu-gcc/g++/gfortran` (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 (cross compiled on x86_64)
- SPEC Compiler: Advance Toolchain 15.0 on x86
- OS: `Ubuntu 20.04.3 LTS`



##  Steps to Run Test

### Step 1: Compile SPEC2017

Compile `x86`, `at` and `ppc` respectively before running this test.
```bash
cp spec-config/*.cfg ${SPEC_HOEM}/config/
runcpu --action=build --config=x86 intrate fprate
runcpu --action=build --config=ppc intrate fprate
runcpu --action=build --config=at  intrate fprate
```

### Step 2: Config Script ENVs

```bash
# Create a copy for running gcc-compiled binaries
cp -r runspec_gem5_power runspec_gem5_power-ppc
# Create a copy for running AT-compiled binaries
cp -r runspec_gem5_power runspec_gem5_power-at
```

Edit `runspec_gem5_power-xxx/Makefile.inc` according to your `SPEC_HOME` and gem5 repo path.

Default LABEL is `ppc`, set it to `at` if you run binaries compiled by AT.

### Step 3: Run Host

Generate host results for comparison.

```bash
cd runspec_gem5_power-xxx/
make -j24 host LABEL=x86
```

### Step 4: Run Gem5

```bash
cd runspec_gem5_power-xxx/
make -j24 gem5
```

If gem5 crashed when running, the corresponding benchmark name will be recorded in `fail_gem5_crash.log`.

### Step 5: Diff Results

After gem5 test finished, check the results.
If there are failed benchmarks, they will be recorded in `fail_gem5_diff.log`.

```bash
cd runspec_gem5_power-xxx/
make diff
# No "FAILED" will show up if all passed
make diff | grep FAILED
```



## Debug Benchmarks Separately

The steps above demonstrate how to run all of the 24 benchmarks together in parallel.

Running test can be very flexible. You can also go to a specific folder to run and debug a single benchmark. 

```bash
# Example
cd runspec_gem5_power-xxx/510.parest_r
make host LABEL=x86
make gem5 && make diff
```



## Tips

If you wanna test different gem5 versions or different SPEC binaries, you can make multiple copies of`runspec_gem5_power` folder for different tests.

Run `make clean-all` to delete everything generated and bring the folder back to its original state.

Run `make help` in `runspec_gem5_power` to get help information.



## Known Issues

- Most host outputs are the same between x86 and power8 except for 508, 510, 527 with minor floating point precision discrepancies. We put these output files from power8 in `ref` folder.

- Output results of floating point precision may differ from binaries compiled by different compilers or the same compiler from different architectures.

