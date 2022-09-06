
include ../Makefile.inc

EXECUTABLE      = roms_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/554.roms_r
ARGS            = < $(BENCH_PATH)/data/test/input/ocean_benchmark0.in.x
ARGS4GEM5       =   $(BENCH_PATH)/data/test/input/ocean_benchmark0.in.x

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) --input "$(ARGS4GEM5)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true

$(EXECUTABLE):
	ln -snf $(BENCH_PATH)/exe/$(EXECUTABLE)
	-make link

link:
	ln -snf $(BENCH_PATH)/data/all/input/varinfo.dat

echo:
	@echo './$(EXECUTABLE) $(ARGS)'

objdump: $(EXECUTABLE)
	$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt

diff:
	@diff host_out.log gem5_out.log >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee -a ../fail_gem5_diff.log ; true

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+
