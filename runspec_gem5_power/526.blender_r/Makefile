
include ../Makefile.inc

EXECUTABLE      = blender_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/526.blender_r
ARGS            = $(BENCH_PATH)/data/test/input/cube.blend --render-output cube_ --threads 1 -b -F RAWTGA -s 1 -e 1 -a

host: $(EXECUTABLE)
	@find -type d -name 'blender_*' -exec rm -rf {} \+;
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log && mv cube_0001.tga cube_0001-host.tga

gem5: $(EXECUTABLE)
	@find -type d -name 'blender_*' -exec rm -rf {} \+;
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)
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
	@diff host_out.log gem5_out.log; true
	@diff cube_0001.tga $(BENCH_PATH)/data/test/compare/cube_0001.org.tga >/dev/null 2>&1 \
		&& echo $$(basename $(BENCH_PATH)) DIFF PASSED \
		|| echo $$(basename $(BENCH_PATH)) DIFF FAILED | tee -a ../fail_gem5_diff.log ; true

ls:
	find -maxdepth 1 -type f -exec ls -lFh {} \+

clean:
	rm -rf *.log *.txt

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+
