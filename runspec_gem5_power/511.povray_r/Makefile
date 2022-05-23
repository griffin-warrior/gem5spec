
include ../Makefile.inc

EXECUTABLE      = povray_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/511.povray_r
ARGS            = $(BENCH_PATH)/data/test/input/SPEC-benchmark-test.ini
FILE			= $(notdir $BENCH_PATH)

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log
	@[ -e SPEC-benchmark.log ] && mv SPEC-benchmark.log SPEC-benchmark_host.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true
	@[ -e SPEC-benchmark.log ] && mv SPEC-benchmark.log SPEC-benchmark_gem5.log

trace: $(EXECUTABLE)
	@echo ---------------------m1 handle ${FILE} beginning ---------------------->${FILE}_trace.log
	$(TIMEH) /opt/at12.0/bin/valgrind --tool=itrace --trace-extent=all --trace-children=no --binary-outfile=$FILE.vgi --num-insns-to-collect=20m ./$(EXECUTABLE) $(ARGS) >>${FILE}_trace.log 2>&1
	$(TIMEH) /opt/at12.0/bin/vgi2qt -f $FILE.vgi -o $FILE.qt  >>${FILE}_trace.log 2>&1
	$(TIMEH) /opt/ibm/sim_ppc/sim_p8/bin/run_timer $FILE.qt 250000 100000 1 $FILE -p 1 -b 1 -e 200 -maximize  >>${FILE}_trace.log 2>&1
	@echo ---------------------m1 handle ${FILE} Finished ---------------------->>${FILE}_trace.log
	@grep -niE "FAIL|ERR|FAULT" ${FILE}_trace.log >> ${FILE}_trace_err.log

pipeview: trace
	@echo ---------------------spv handle ${FILE} beginning ---------------------->>${FILE}_trace.log
	$(TIMEH) /opt/ibm/sim_ppc/bin/scrollpv -pipe $FILE.pipe -config $FILE.config  >>${FILE}_trace.log 2>&1
	@echo ---------------------spv handle ${FILE} beginning ---------------------->>${FILE}_trace.log
	@grep -niE "FAIL|ERR|FAULT" ${FILE}_trace.log >> ${FILE}_trace_err.log

$(EXECUTABLE):
	ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)
	-make link

link:
	ln -s $(BENCH_PATH)/data/test/input/SPEC-benchmark-test.pov
	find $(BENCH_PATH)/data/all/input/*.inc -type f -exec ln -s {} \;

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
	rm -rf *.log *.txt *.tga *.out *.vgi *.qt *.dir *.config *.results *.pipe *.simpts *.weights *.merge

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+
