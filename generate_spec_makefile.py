#!/usr/bin/env python3

import os, sys
import time

# Global VARs
# TODO 
spec_path = '/home/dell/cpu2017'
cpu_path = spec_path + '/benchspec/CPU'
# TODO Edit your label
label = 'ppc'

# TODO gem5 repo path
gem5_path = '/home/dell/prj/gem5'
# isa = 'X86'
isa = 'POWER'
gem5_exe = 'gem5.opt'
gem5_py = 'configs/example/se.py'


list_bench = []
# LIST DEFINITION: [0]code, [1]name/dir, [2]exe, [3]bench_folder, [4]binary, [5]exe-args
list_bench.append(['500', 'perlbench_r', 'perlbench_r' , '', '', '-I. -I$(BENCH_PATH)/lib $(BENCH_PATH)/data/test/input/makerand.pl'])
list_bench.append(['502', 'gcc_r'      , 'cpugcc_r'    , '', '', '$(BENCH_PATH)/data/test/input/t1.c -finline-limit=50000 -o t1.o[ts-03_-finline-limit_50000.s'])
list_bench.append(['503', 'bwaves_r'   , 'bwaves_r'    , '', '', '< $(BENCH_PATH)/data/test/input/bwaves_1.in'])
list_bench.append(['505', 'mcf_r'      , 'mcf_r'       , '', '', '$(BENCH_PATH)/data/test/input/inp.in'])
list_bench.append(['507', 'cactuBSSN_r', 'cactusBSSN_r', '', '', '$(BENCH_PATH)/data/test/input/spec_test.par'])
list_bench.append(['508', 'namd_r'     , 'namd_r'      , '', '', '--input $(BENCH_PATH)/data/all/input/apoa1.input --iterations 2 --output apoa1.test.output'])
list_bench.append(['510', 'parest_r'   , 'parest_r'    , '', '', '$(BENCH_PATH)/data/test/input/test.prm'])
list_bench.append(['511', 'povray_r'   , 'povray_r'    , '', '', '$(BENCH_PATH)/data/test/input/SPEC-benchmark-test.ini'])
list_bench.append(['519', 'lbm_r'      , 'lbm_r'       , '', '', '20 reference.dat 0 1 100_100_130_cf_a.of'])
list_bench.append(['520', 'omnetpp_r'  , 'omnetpp_r'   , '', '', '-c General -r 0'])
list_bench.append(['521', 'wrf_r'      , 'wrf_r'       , '', '', ''])
list_bench.append(['523', 'xalancbmk_r', 'cpuxalan_r'  , '', '', '-v $(BENCH_PATH)/data/test/input/test.xml $(BENCH_PATH)/data/test/input/xalanc.xsl'])
list_bench.append(['525', 'x264_r'     , 'x264_r'      , '', '', '--dumpyuv 50 --frames 156 -o BuckBunny_New.264 $(BENCH_PATH)/data/test/input/BuckBunny.264 1280x720'])
list_bench.append(['526', 'blender_r'  , 'blender_r'   , '', '', '$(BENCH_PATH)/data/test/input/cube.blend --render-output cube_ --threads 1 -b -F RAWTGA -s 1 -e 1 -a'])
list_bench.append(['527', 'cam4_r'     , 'cam4_r'      , '', '', ''])
list_bench.append(['531', 'deepsjeng_r', 'deepsjeng_r' , '', '', '$(BENCH_PATH)/data/test/input/test.txt'])
list_bench.append(['538', 'imagick_r'  , 'imagick_r'   , '', '', '-limit disk 0 $(BENCH_PATH)/data/test/input/test_input.tga -shear 25 -resize 640x480 -negate -alpha Off test_output.tga'])
list_bench.append(['541', 'leela_r'    , 'leela_r'     , '', '', '$(BENCH_PATH)/data/test/input/test.sgf'])
list_bench.append(['544', 'nab_r'      , 'nab_r'       , '', '', 'hkrdenq 1930344093 1000'])
list_bench.append(['548', 'exchange2_r', 'exchange2_r' , '', '', '0'])
list_bench.append(['549', 'fotonik3d_r', 'fotonik3d_r' , '', '', ''])
list_bench.append(['554', 'roms_r'     , 'roms_r'      , '', '', '< $(BENCH_PATH)/data/test/input/ocean_benchmark0.in.x'])
list_bench.append(['557', 'xz_r'       , 'xz_r'        , '', '', '$(BENCH_PATH)/data/all/input/cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1548636 15553480'])
#list_bench.append(['628', 'pop2_s'     , 'speed_pop2'  , '', '', ''])
list_bench.append(['999', 'specrand_ir', 'specrand_ir' , '', '', '324342 24239'])



def gen_makefile(report_dir, label):
    for index, bench in enumerate(list_bench):
        list_bench[index][3] = bench[0] + '.' + bench[1]
        list_bench[index][4] = bench[2] + '_base.' + label
    report_abspath = os.path.abspath(report_dir)
    error_log_file = report_abspath + '/error_' + label + '.log'
    for bench in list_bench:
        report_bench_abspath = report_abspath + '/' + bench[3]
        os.makedirs(report_bench_abspath, 0o755) 
        makefile = open(report_bench_abspath + '/' + 'Makefile', 'w')
        makefile.write('\n' + 'include ../Makefile.inc')
        makefile.write('\n')
        makefile.write('\n' + 'EXECUTABLE      = ' + bench[2] + '_base.$(LABEL)')
        makefile.write('\n' + 'BENCH_PATH      = ' + '$(SPEC_HOME)/benchspec/CPU' + '/' + bench[3])
        makefile.write('\n' + 'ARGS            = ' + bench[5])
        makefile.write('\n')
        makefile.write('\n' + 'host: $(EXECUTABLE)')
        makefile.write('\n' + '\t' + '$(TIMEH) ./$(EXECUTABLE) $(ARGS) 1> host_out.log 2> host_err.log')
        makefile.write('\n')
        makefile.write('\n' + 'gem5: $(EXECUTABLE)')
        makefile.write('\n' + '\t' + '$(TIMEG) $(GEM5) $(GEM5_OPT) $(GEM5_PY) -c $(EXECUTABLE) -o " $(ARGS)" $(GEM5_PY_OPT)')
        makefile.write('\n' + '\t' + '@chmod -x *gem5.log')
        makefile.write('\n' + '\t' + 'grep -nr "^Error" stderr_gem5.log && echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_crash.log ; true')
        makefile.write('\n')
        makefile.write('\n' + '$(EXECUTABLE):')
        makefile.write('\n' + '\t' + 'ln -s $(BENCH_PATH)/exe/$(EXECUTABLE)')
        makefile.write('\n')
        makefile.write('\n' + 'link:')
        makefile.write('\n')
        makefile.write('\n' + 'echo:')
        makefile.write('\n' + '\t' + '@echo \'./$(EXECUTABLE) $(ARGS)\'')
        makefile.write('\n')
        makefile.write('\n' + 'objdump: $(EXECUTABLE)')
        makefile.write('\n' + '\t' + '$(OBJDUMP) -d ./$(EXECUTABLE) > obj.txt')
        makefile.write('\n')
        makefile.write('\n' + 'diff:')
        makefile.write('\n' + '\t' + '@diff host_out.log gem5_out.log >/dev/null 2>&1 || echo $$(basename $(BENCH_PATH)) >> ../fail_gem5_diff.log ; true')
        makefile.write('\n')
        makefile.write('\n' + 'ls:')
        makefile.write('\n' + '\t' + 'find -type f -exec ls -lFh {} \+')
        makefile.write('\n')
        makefile.write('\n' + 'clean:')
        makefile.write('\n' + '\t' + 'rm -rf *.log *.txt')
        makefile.write('\n')
        makefile.write('\n' + 'clean-all:')
        makefile.write('\n' + '\t' + 'find ./* ! -name Makefile -exec rm -rf {} \+')
        makefile.write('\n')
    makefile.close()



if __name__ == '__main__':

    time_str = time.strftime("%Y%m%d_%H-%M-%S", time.localtime())

    report_dir = 'runspec_gen_' + label # + '_' + time_str
    if os.path.exists(report_dir):
        print('Report Directory ' + report_dir + ' Exists! Quit...')
        exit()

    gen_makefile(report_dir, label)

    # Generate Makefile.inc
    os.makedirs(report_dir, 0o755, exist_ok = True) 
    makefile_inc = open(report_dir + '/Makefile.inc', 'w')
    makefile_inc.write('\n' + 'SPEC_HOME      ?= ' + spec_path)
    makefile_inc.write('\n' + 'LABEL          ?= ppc')
    makefile_inc.write('\n')

    makefile_inc.write('\n' + 'GEM5_REPO_PATH ?= ' + gem5_path)
    makefile_inc.write('\n' + 'GEM5            = ' + '$(GEM5_REPO_PATH)/build/' + isa + '/' + gem5_exe)
    makefile_inc.write('\n' + 'GEM5_OPT       += ' + '--redirect-stdout')
    makefile_inc.write('\n' + 'GEM5_OPT       += ' + '--stdout-file=../stdout_gem5.log')
    makefile_inc.write('\n' + 'GEM5_OPT       += ' + '--redirect-stderr')
    makefile_inc.write('\n' + 'GEM5_OPT       += ' + '--stderr-file=../stderr_gem5.log')
    makefile_inc.write('\n' + '# GEM5_OPT       += ' + '--debug-flags=SyscallAll,Fetch')
    makefile_inc.write('\n')
    makefile_inc.write('\n' + 'GEM5_PY         = ' + '$(GEM5_REPO_PATH)/configs/example/se.py')
    makefile_inc.write('\n' + 'GEM5_PY_OPT    += ' + '--output=../gem5_out.log')
    makefile_inc.write('\n' + 'GEM5_PY_OPT    += ' + '--mem-size=16384MB')
    makefile_inc.write('\n')

    makefile_inc.write('\n' + '# OBJDUMP         = objdump')
    makefile_inc.write('\n' + 'OBJDUMP         = /opt/at15.0/bin/powerpc64le-linux-gnu-objdump')
    makefile_inc.write('\n')

    makefile_inc.write('\n' + 'TIMEH           = /usr/bin/time --format="Host Consumed Time: %E"')
    makefile_inc.write('\n' + 'TIMEG           = /usr/bin/time --format="GEM5 Consumed Time: %E"')
    makefile_inc.write('\n')
    makefile_inc.close()

    # Generate Root Makefile
    makefile = open(report_dir + '/Makefile', mode='w', newline='')
    makefile.write('\n' + '.PHONY: all')
    makefile.write('\n')
    makefile.write('\n' + 'all: help')
    makefile.write('\n')
    makefile.write('\n' + 'host:')
    for bench in list_bench:
        makefile.write(' host_' + bench[0])
    makefile.write('\n')

    makefile.write('\n' + 'gem5:')
    for bench in list_bench:
        makefile.write(' gem5_' + bench[0])
    makefile.write('\n')

    for bench in list_bench:
        makefile.write('\n' + 'host_' + bench[0] + ':')
        makefile.write('\n' + '\t' + '@cd  ' + bench[3] + '; make host || echo ' + bench[3] + ' >> ../fail_host.log')
    makefile.write('\n')

    for bench in list_bench:
        makefile.write('\n' + 'gem5_' + bench[0] + ':')
        makefile.write('\n' + '\t' + '@-make gem5 -C ' + bench[3])
    makefile.write('\n')

    makefile.write('\n' + 'diff:')
    makefile.write('\n' + '\t' + 'find -type d -regex ".*r" -exec make diff -C {} \;')
    makefile.write('\n')

    makefile.write('\n' + 'clean:')
    makefile.write('\n' + '\t' + 'rm -rf *.log')
    makefile.write('\n' + '\t' + 'find -type d -regex ".*r" -exec make clean -C {} \;')
    #for bench in list_bench:
    #    makefile.write('\n' + '\t' + 'make clean -C ' + bench[3])
    makefile.write('\n')

    makefile.write('\n' + 'clean-all:')
    makefile.write('\n' + '\t' + 'rm -rf *.log')
    makefile.write('\n' + '\t' + 'find -type d -regex ".*r" -exec make clean-all -C {} \;')
    #for bench in list_bench:
    #    makefile.write('\n' + '\t' + 'make clean_all -C ' + bench[3])
    makefile.write('\n')

    makefile.write('\n' + 'time:')
    makefile.write('\n' + '\t' + '@echo grep -nr \"^Host Consumed Time:\"')
    makefile.write('\n' + '\t' + '@grep -nr "^Host Consumed Time:" | sort -h| sed "s/\..\+: /,/g" || true')
    makefile.write('\n' + '\t' + '@echo grep -nr \"^GEM5 Consumed Time:\"')
    makefile.write('\n' + '\t' + '@grep -nr "^GEM5 Consumed Time:" | sort -h| sed "s/\..\+: /,/g" || true')
    makefile.write('\n')

    makefile.write('\n' + 'help:')
    makefile.write('\n' + '\t' + '@echo "Modify SPEC and GEM5 path in Makefile.inc before run!"')
    makefile.write('\n' + '\t' + '@echo "Use -jN to run multiple benchmarks in parallel"')
    makefile.write('\n' + '\t' + '@echo ""')
    makefile.write('\n' + '\t' + '@echo "  Run all SPEC on host:"')
    makefile.write('\n' + '\t' + '@echo "    make host -jN"')
    makefile.write('\n' + '\t' + '@echo "  Run all SPEC via GEM5:"')
    makefile.write('\n' + '\t' + '@echo "    make gem5 -jN"')
    makefile.write('\n' + '\t' + '@echo "  Clean log and temp files:"')
    makefile.write('\n' + '\t' + '@echo "    make clean"')
    makefile.write('\n' + '\t' + '@echo "  Clean all except Makefile:"')
    makefile.write('\n' + '\t' + '@echo "    make clean-all"')
    makefile.write('\n' + '\t' + '@echo "  Get consumed runtime:"')
    makefile.write('\n' + '\t' + '@echo "    make time"')
    makefile.write('\n' + '\t' + '@echo ""')
    makefile.write('\n' + '\t' + '@echo "Check fail_[host|gem5].log to see failed benchmarks."')
    makefile.write('\n' + '\t' + '@echo ""')
    makefile.write('\n')

    makefile.close()

