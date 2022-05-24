DATE = $(shell date +%Y%m%d%H%M%S)
GEM5_REPO_PATH = $(shell awk '$$1=="GEM5_REPO_PATH"{print $$3}' Makefile.inc)

.PHONY: all

all: help

host: host_500 host_502 host_503 host_505 host_507 host_508 host_510 host_511 host_519 host_520 host_521 host_523 host_525 host_526 host_527 host_531 host_538 host_541 host_544 host_548 host_549 host_554 host_557 host_999

gem5: log-pre gem5_500 gem5_502 gem5_503 gem5_505 gem5_507 gem5_508 gem5_510 gem5_511 gem5_519 gem5_520 gem5_521 gem5_523 gem5_525 gem5_526 gem5_527 gem5_531 gem5_538 gem5_541 gem5_544 gem5_548 gem5_549 gem5_554 gem5_557 gem5_999
	@make log-post

trace: trace_500 trace_502 trace_503 trace_505 trace_507 trace_508 trace_510 trace_511 trace_519 trace_520 trace_521 trace_523 trace_525 trace_526 trace_527 trace_531 trace_538 trace_541 trace_544 trace_548 trace_549 trace_554 trace_557 trace_999

log-pre:
	@LOG_DIR=$(DATE); \
	echo $(DATE) > DATE.log; \
	mkdir -p log/$${LOG_DIR}; \
	echo  $(GEM5_REPO_PATH) > log/$${LOG_DIR}/summary.txt; \
	git -C $(GEM5_REPO_PATH) log -1 --pretty=oneline >> log/$${LOG_DIR}/summary.txt; \
	echo  >> log/$${LOG_DIR}/summary.txt; \
	git -C $(GEM5_REPO_PATH) status >> log/$${LOG_DIR}/summary.txt; \
	echo  >> log/$${LOG_DIR}/summary.txt; \
	cat Makefile.inc >> log/$${LOG_DIR}/summary.txt

log-post:
	@LOG_DIR=$$(cat DATE.log); \
	mkdir -p log/$${LOG_DIR}; \
	BENCH_LIST=$$(find -maxdepth 1 -type d -regex ".*r" -exec basename {} \; | sort -h); \
	for name in $${BENCH_LIST}; do \
		[[ -e $${name}/m5out/config.ini ]] || continue; \
		mkdir -p log/$${LOG_DIR}/$${name}; \
		[[ -e $${name}/gem5_stats.log   ]] && cp $${name}/gem5_stats.log   log/$${LOG_DIR}/$${name}/; \
		[[ -e $${name}/stderr_gem5.log  ]] && cp $${name}/stderr_gem5.log  log/$${LOG_DIR}/$${name}/; \
		[[ -e $${name}/stdout_gem5.log  ]] && cp $${name}/stdout_gem5.log  log/$${LOG_DIR}/$${name}/; \
		[[ -e $${name}/m5out/config.ini ]] && cp $${name}/m5out/config.ini log/$${LOG_DIR}/$${name}/; \
	done

host_500:
	@cd  500.perlbench_r; make host || echo 500.perlbench_r >> ../fail_host.log
host_502:
	@cd  502.gcc_r; make host || echo 502.gcc_r >> ../fail_host.log
host_503:
	@cd  503.bwaves_r; make host || echo 503.bwaves_r >> ../fail_host.log
host_505:
	@cd  505.mcf_r; make host || echo 505.mcf_r >> ../fail_host.log
host_507:
	@cd  507.cactuBSSN_r; make host || echo 507.cactuBSSN_r >> ../fail_host.log
host_508:
	@cd  508.namd_r; make host || echo 508.namd_r >> ../fail_host.log
host_510:
	@cd  510.parest_r; make host || echo 510.parest_r >> ../fail_host.log
host_511:
	@cd  511.povray_r; make host || echo 511.povray_r >> ../fail_host.log
host_519:
	@cd  519.lbm_r; make host || echo 519.lbm_r >> ../fail_host.log
host_520:
	@cd  520.omnetpp_r; make host || echo 520.omnetpp_r >> ../fail_host.log
host_521:
	@cd  521.wrf_r; make host || echo 521.wrf_r >> ../fail_host.log
host_523:
	@cd  523.xalancbmk_r; make host || echo 523.xalancbmk_r >> ../fail_host.log
host_525:
	@cd  525.x264_r; make host || echo 525.x264_r >> ../fail_host.log
host_526:
	@cd  526.blender_r; make host || echo 526.blender_r >> ../fail_host.log
host_527:
	@cd  527.cam4_r; make host || echo 527.cam4_r >> ../fail_host.log
host_531:
	@cd  531.deepsjeng_r; make host || echo 531.deepsjeng_r >> ../fail_host.log
host_538:
	@cd  538.imagick_r; make host || echo 538.imagick_r >> ../fail_host.log
host_541:
	@cd  541.leela_r; make host || echo 541.leela_r >> ../fail_host.log
host_544:
	@cd  544.nab_r; make host || echo 544.nab_r >> ../fail_host.log
host_548:
	@cd  548.exchange2_r; make host || echo 548.exchange2_r >> ../fail_host.log
host_549:
	@cd  549.fotonik3d_r; make host || echo 549.fotonik3d_r >> ../fail_host.log
host_554:
	@cd  554.roms_r; make host || echo 554.roms_r >> ../fail_host.log
host_557:
	@cd  557.xz_r; make host || echo 557.xz_r >> ../fail_host.log
host_999:
	@cd  999.specrand_ir; make host || echo 999.specrand_ir >> ../fail_host.log

gem5_500:
	@-make gem5 -C 500.perlbench_r
gem5_502:
	@-make gem5 -C 502.gcc_r
gem5_503:
	@-make gem5 -C 503.bwaves_r
gem5_505:
	@-make gem5 -C 505.mcf_r
gem5_507:
	@-make gem5 -C 507.cactuBSSN_r
gem5_508:
	@-make gem5 -C 508.namd_r
gem5_510:
	@-make gem5 -C 510.parest_r
gem5_511:
	@-make gem5 -C 511.povray_r
gem5_519:
	@-make gem5 -C 519.lbm_r
gem5_520:
	@-make gem5 -C 520.omnetpp_r
gem5_521:
	@-make gem5 -C 521.wrf_r
gem5_523:
	@-make gem5 -C 523.xalancbmk_r
gem5_525:
	@-make gem5 -C 525.x264_r
gem5_526:
	@-make gem5 -C 526.blender_r
gem5_527:
	@-make gem5 -C 527.cam4_r
gem5_531:
	@-make gem5 -C 531.deepsjeng_r
gem5_538:
	@-make gem5 -C 538.imagick_r
gem5_541:
	@-make gem5 -C 541.leela_r
gem5_544:
	@-make gem5 -C 544.nab_r
gem5_548:
	@-make gem5 -C 548.exchange2_r
gem5_549:
	@-make gem5 -C 549.fotonik3d_r
gem5_554:
	@-make gem5 -C 554.roms_r
gem5_557:
	@-make gem5 -C 557.xz_r
gem5_999:
	@-make gem5 -C 999.specrand_ir

trace_500:
	@-make trace -C 500.perlbench_r
trace_502:
	@-make trace -C 502.gcc_r
trace_503:
	@-make trace -C 503.bwaves_r
trace_505:
	@-make trace -C 505.mcf_r
trace_507:
	@-make trace -C 507.cactuBSSN_r
trace_508:
	@-make trace -C 508.namd_r
trace_510:
	@-make trace -C 510.parest_r
trace_511:
	@-make trace -C 511.povray_r
trace_519:
	@-make trace -C 519.lbm_r
trace_520:
	@-make trace -C 520.omnetpp_r
trace_521:
	@-make trace -C 521.wrf_r
trace_523:
	@-make trace -C 523.xalancbmk_r
trace_525:
	@-make trace -C 525.x264_r
trace_526:
	@-make trace -C 526.blender_r
trace_527:
	@-make trace -C 527.cam4_r
trace_531:
	@-make trace -C 531.deepsjeng_r
trace_538:
	@-make trace -C 538.imagick_r
trace_541:
	@-make trace -C 541.leela_r
trace_544:
	@-make trace -C 544.nab_r
trace_548:
	@-make trace -C 548.exchange2_r
trace_549:
	@-make trace -C 549.fotonik3d_r
trace_554:
	@-make trace -C 554.roms_r
trace_557:
	@-make trace -C 557.xz_r
trace_999:
	@-make trace -C 999.specrand_ir

diff:
	find -maxdepth 1 -type d -regex ".*r" -exec make diff -C {} \;

clean:
	rm -rf *.log
	find -maxdepth 1 -type d -regex ".*r" -exec make clean -C {} \;

clean-all:
	rm -rf *.log
	find -maxdepth 1 -type d -regex ".*r" -exec make clean-all -C {} \;

time:
	@echo grep -nr "^Host Consumed Time:"
	@grep -nr "^Host Consumed Time:" | sort -h| sed "s/\..\+: /,/g" || true
	@echo grep -nr "^GEM5 Consumed Time:"
	@grep -nr "^GEM5 Consumed Time:" | sort -h| sed "s/\..\+: /,/g" || true

help:
	@echo "Modify SPEC and GEM5 path in Makefile.inc before run!"
	@echo "Use -jN to run multiple benchmarks in parallel"
	@echo ""
	@echo "  Run all SPEC on host:"
	@echo "    make host -jN"
	@echo "  Run all SPEC via GEM5:"
	@echo "    make gem5 -jN"
	@echo "  Clean log and temp files:"
	@echo "    make clean"
	@echo "  Clean all except Makefile:"
	@echo "    make clean-all"
	@echo "  Get consumed runtime:"
	@echo "    make time"
	@echo ""
	@echo "Check fail_[host|gem5].log to see failed benchmarks."
	@echo ""

