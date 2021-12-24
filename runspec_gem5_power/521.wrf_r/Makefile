
include ../Makefile.inc

EXECUTABLE      = wrf_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/521.wrf_r
ARGS            = 

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true

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
	@[ $$(uname -m) == x86_64 ] \
		&& $(BENCH_PATH)/exe/diffwrf_521_base.x86 wrfout_d01_2000-01-24_12_10_00 $(BENCH_PATH)/data/test/compare/wrf_reference_01 > diff.txt \
		|| $(BENCH_PATH)/exe/diffwrf_521_base.$(LABEL) wrfout_d01_2000-01-24_12_10_00 $(BENCH_PATH)/data/test/compare/wrf_reference_01 > diff.txt
	@sed -i 's/Just plot  F/Just plot   F/g' diff.txt
	@diff diff.txt $(BENCH_PATH)/data/test/output/diffwrf_output_01.txt >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee ../fail_gem5_diff.log

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt wrfout* namelist.output

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+
