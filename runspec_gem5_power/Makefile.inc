
SPEC_HOME      ?= /home/dell/cpu2017
LABEL          ?= ppc

GEM5_REPO_PATH ?= /home/dell/prj/gem5
GEM5            = $(GEM5_REPO_PATH)/build/POWER/gem5.opt
GEM5_OPT       += --redirect-stdout
GEM5_OPT       += --stdout-file=../stdout_gem5.log
GEM5_OPT       += --redirect-stderr
GEM5_OPT       += --stderr-file=../stderr_gem5.log
GEM5_OPT       += --stats-file=../gem5_stats.log
# GEM5_OPT       += --debug-flags=SyscallAll,Fetch

GEM5_PY         = $(GEM5_REPO_PATH)/configs/example/se.py
GEM5_PY_OPT    += --output=../gem5_out.log
GEM5_PY_OPT    += --mem-size=16384MB
# for O3 only, Real Power8 Cache Size
GEM5_PY_OPT    += --cpu-type=DerivO3CPU --ruby --caches --l1d_size=64kB --l1d_assoc=8 --l1i_size=32kB --l1i_assoc=8 --l2_size=512kB --l2_assoc=8 --l3_size=8mB --l3_assoc=8 --cacheline_size=128

# OBJDUMP         = objdump
OBJDUMP         = /opt/at15.0/bin/powerpc64le-linux-gnu-objdump

TIMEH           = /usr/bin/time --format="Host Consumed Time: %E  --  $$(basename $${PWD})"
TIMEG           = /usr/bin/time --format="GEM5 Consumed Time: %E  --  $$(basename $${PWD})"

SHELL          := /bin/bash

