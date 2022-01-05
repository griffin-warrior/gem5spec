
SPEC_HOME      ?= /home/dell/cpu2017
LABEL          ?= ppc

GEM5_REPO_PATH ?= /home/dell/prj/gem5
GEM5            = $(GEM5_REPO_PATH)/build/POWER/gem5.opt
GEM5_OPT       += --redirect-stdout
GEM5_OPT       += --stdout-file=../stdout_gem5.log
GEM5_OPT       += --redirect-stderr
GEM5_OPT       += --stderr-file=../stderr_gem5.log
# GEM5_OPT       += --debug-flags=SyscallAll,Fetch

GEM5_PY         = $(GEM5_REPO_PATH)/configs/example/se.py
GEM5_PY_OPT    += --output=../gem5_out.log
GEM5_PY_OPT    += --mem-size=16384MB

# OBJDUMP         = objdump
OBJDUMP         = /opt/at15.0/bin/powerpc64le-linux-gnu-objdump

TIMEH           = /usr/bin/time --format="Host Consumed Time: %E"
TIMEG           = /usr/bin/time --format="GEM5 Consumed Time: %E"

SHELL          := /bin/bash

