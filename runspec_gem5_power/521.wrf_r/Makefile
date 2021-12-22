
include ../Makefile.inc

EXECUTABLE      = wrf_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/521.wrf_r
ARGS            = 

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true

$(EXECUTABLE):
	ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)
	-make link

link:
	ln -s $(BENCH_PATH)/data/test/input/namelist.input
	find $(BENCH_PATH)/data/all/input/* -type f -exec ln -s {} \;

echo:
	@echo './$(EXECUTABLE) $(ARGS)'

objdump: $(EXECUTABLE)
	$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt

diff:
	@diff host_out.log gem5_out.log >/dev/null 2>&1 || echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_diff.log ; true

ls:
	find -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt wrfout* namelist.output

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+