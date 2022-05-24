
include ../Makefile.inc

EXECUTABLE      = fotonik3d_r_base.$(LABEL)
BENCH_PATH      = $(SPEC_HOME)/benchspec/CPU/549.fotonik3d_r
ARGS            = 

host: $(EXECUTABLE)
	$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log

gem5: $(EXECUTABLE)
	$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) $(GEM5_PY_OPT)
	@chmod -x *gem5.log
	@grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true

$(EXECUTABLE):
	ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)
	-make link

link:
	find $(BENCH_PATH)/data/test/input/* -type f -exec ln -s {} \;
	[ -e OBJ.dat ] || unxz -f OBJ.dat.xz

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
	rm -rf *.log *.txt *.out

clean-all:
	find ./* ! -name Makefile -exec rm -rf {} \+

include ../M1.inc