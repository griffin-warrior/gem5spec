
include ../Makefile.inc

EXECUTABLE      = namd_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/508.namd_r
ARGS            = --input $(BENCH_PATH)/data/all/input/apoa1.input --iterations 2 --output apoa1.test.host.output
ARGS4GEM5       = --input $(BENCH_PATH)/data/all/input/apoa1.input --iterations 2 --output apoa1.test.gem5.output

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log
	@sed -i 's/host\.//g' host_out.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS4GEM5)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true
	@sed -i 's/gem5\.//g' gem5_out.log

$(EXECUTABLE):
	ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)

link:

echo:
	@echo './$(EXECUTABLE) $(ARGS)'

objdump: $(EXECUTABLE)
	$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt

diff:
	@diff host_out.log gem5_out.log >/dev/null 2>&1 \
		&& diff apoa1.test.gem5.output ../ref/508/apoa1.test.host.ppc.output >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee -a ../fail_gem5_diff.log ; true

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+

include ../M1.inc