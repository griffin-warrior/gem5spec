
include ../Makefile.inc

EXECUTABLE      = povray_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/511.povray_r
ARGS            = $(BENCH_PATH)/data/test/input/SPEC-benchmark-test.ini
FILE            = $$(basename $(BENCH_PATH))
#Simpoint
INTERVAL_SIZE   =100000
#ITRACE
NUM_INSNS =20m
#vgi2qt
JUMP_NUM_100m      =0
CONVERT_NUM_Vgi_RECS_100m   =1
#Runtimer
NUM_INST          =250000
CPI_INTERVAL      =100000
RESET_STATS       =1
SCROLL_PIPE       =1
SCROLL_BEGIN      =1
SCROLL_END        =200

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log
	@[ -e SPEC-benchmark.log ] && mv SPEC-benchmark.log SPEC-benchmark_host.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true
	@[ -e SPEC-benchmark.log ] && mv SPEC-benchmark.log SPEC-benchmark_gem5.log

simpoint: $(EXECUTABLE)
	@echo ---------------------simpt handle $(FILE) beginning ---------------------->$(FILE)_trace.log
	$(TIMEH) /opt/at12.0/bin/valgrind --tool=exp-bbv --interval-size=$(INTERVAL_SIZE) --bb-out-file=$(FILE).bb.out ./$(EXECUTABLE) $(ARGS) >>$(FILE)_trace.log 2>&1 ; \
	MAXK=`wc -l $(FILE).bb.out | awk 'END{print sqrt($$1)}'` ; \
	/home/lizongping/Desktop/SimPoint.3.2/bin/simpoint -loadFVFile $(FILE).bb.out -maxK $${MAXK} -saveSimpoints ./$(FILE).simpts -saveSimpointWeights ./$(FILE).weights >>$(FILE)_trace.log 2>&1 ; \
	paste $(FILE).simpts $(FILE).weights | awk '{printf "%-20d %-20d %-15.5f\n",$$2,$$1,$$3}' 1>$(FILE).merge ; \
	sort $(FILE).merge -n -k 2 -o $(FILE).merge 2>>$(FILE)_trace.log
	@echo ---------------------simpt handle $(FILE) Finished ---------------------->>$(FILE)_trace.log
	@-grep -niE "FAIL|ERR|FAULT" $(FILE)_trace.log > $(FILE)_trace_err.log

trace: simpoint
	@echo ---------------------m1 handle $(FILE) beginning ---------------------->>$(FILE)_trace.log
	$(TIMEH) /opt/at12.0/bin/valgrind --tool=itrace --trace-extent=all --trace-children=no --binary-outfile=$(FILE).vgi --num-insns-to-collect=$(NUM_INSNS) ./$(EXECUTABLE) $(ARGS) >>$(FILE)_trace.log 2>&1 ; \
	/opt/at12.0/bin/vgi2qt -f $(FILE).vgi -o $(FILE).qt  >>$(FILE)_trace.log 2>&1 ; \
	/opt/ibm/sim_ppc/sim_p8/bin/run_timer $(FILE).qt $(NUM_INST) $(CPI_INTERVAL) $(RESET_STATS) $(FILE) -p $(SCROLL_PIPE) -b $(SCROLL_BEGIN) -e $(SCROLL_END) -maximize  >>$(FILE)_trace.log 2>&1
	@echo ---------------------m1 handle $(FILE) Finished ---------------------->>$(FILE)_trace.log
	@-grep -niE "FAIL|ERR|FAULT" $(FILE)_trace.log > $(FILE)_trace_err.log

pipeview: trace
	@echo ---------------------spv handle $(FILE) beginning ---------------------->>$(FILE)_trace.log
	$(TIMEH) /opt/ibm/sim_ppc/bin/scrollpv -pipe $(FILE).pipe -config $(FILE).config  >>$(FILE)_trace.log 2>&1
	@echo ---------------------spv handle $(FILE) beginning ---------------------->>$(FILE)_trace.log
	@-grep -niE "FAIL|ERR|FAULT" $(FILE)_trace.log > $(FILE)_trace_err.log

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
	rm -rf *.log *.txt *.tga *.simpts *.weights *.merge *.out *.vgi *.qt *.dir *.config *.results *.pipe

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+
