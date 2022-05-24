
include ../Makefile.inc

EXECUTABLE      = cam4_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/527.cam4_r
ARGS            = 

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true
	@sed -i 's/DATE.\+TIME.\+//g' gem5_out.log

$(EXECUTABLE):
	ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)
	-make link

link:
	ln -s $(BENCH_PATH)/data/test/input/drv_in
	ln -s $(BENCH_PATH)/data/test/input/atm_in
	find $(BENCH_PATH)/data/all/input/* -type f -exec ln -s {} \;

echo:
	@echo './$(EXECUTABLE) $(ARGS)'

objdump: $(EXECUTABLE)
	$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt

diff:
	@diff ../ref/527/host_ppc_out.log gem5_out.log >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee -a ../fail_gem5_diff.log ; true

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt  ccsm_timing h0.nc

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+

include ../M1.inc