
include ../Makefile.inc

EXECUTABLE      = cpugcc_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/502.gcc_r
ARGS            = $(BENCH_PATH)/data/test/input/t1.c -finline-limit=50000 -o host_out.s
ARGS4GEM5       = $(BENCH_PATH)/data/test/input/t1.c -finline-limit=50000 -o gem5_out.s

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS4GEM5)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true

$(EXECUTABLE):
	ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)

link:

echo:
	@echo './$(EXECUTABLE) $(ARGS)'

objdump: $(EXECUTABLE)
	$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt

diff:
	@diff host_out.s gem5_out.s >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee -a ../fail_gem5_diff.log ; true

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+
