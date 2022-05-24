
include ../Makefile.inc

EXECUTABLE      = x264_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/525.x264_r
ARGS            = --dumpyuv 50 --frames 156 -o BuckBunny_New-host.264 $(BENCH_PATH)/data/test/input/BuckBunny.264 1280x720
ARGS4GEM5       = --dumpyuv 50 --frames 156 -o BuckBunny_New-gem5.264 $(BENCH_PATH)/data/test/input/BuckBunny.264 1280x720

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS4GEM5)" $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true

$(EXECUTABLE):
	ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)

link:

echo:
	@echo './$(EXECUTABLE) $(ARGS)'

objdump: $(EXECUTABLE)
	$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt

diff:
	@diff BuckBunny_New-host.264 BuckBunny_New-gem5.264 >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee -a ../fail_gem5_diff.log ; true

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+

include ../M1.inc