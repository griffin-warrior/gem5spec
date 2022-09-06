
include ../Makefile.inc

EXECUTABLE      = povray_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/511.povray_r
ARGS            = $(BENCH_PATH)/data/test/input/SPEC-benchmark-test.ini

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log
	@[ -e SPEC-benchmark.log ] && mv SPEC-benchmark.log SPEC-benchmark_host.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true
	@[ -e SPEC-benchmark.log ] && mv SPEC-benchmark.log SPEC-benchmark_gem5.log


$(EXECUTABLE):
	ln -snf $(BENCH_PATH)/exe/$(EXECUTABLE)
	-make link

link:
	ln -snf $(BENCH_PATH)/data/test/input/SPEC-benchmark-test.pov
	find $(BENCH_PATH)/data/all/input/*.inc -type f -exec ln -snf {} \;

echo:
	@echo './$(EXECUTABLE) $(ARGS)'

objdump: $(EXECUTABLE)
	$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt

diff:
	@diff SPEC-benchmark_host.log SPEC-benchmark_gem5.log >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee -a ../fail_gem5_diff.log ; true

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt *.tga

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+
