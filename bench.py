#!/usr/bin/env python3
import os
import pyperf


def func():
    os.system("bash repro.sh")


runner = pyperf.Runner()
runner.bench_func("bug_benchmark", func)
