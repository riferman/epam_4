#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Syarhey Matusevich"


def arange(start, stop=None, step=1):
    if stop is None:  # If there is no y value: range(x)
        stop = start
        start = 0
    if start > stop:
        if step >= 0:
            raise TypeError("step >= 0")
    if start < stop:
        if step <= 0:
            raise TypeError("step <= 0")
    if not isinstance(start, int):
        raise TypeError("input must be a long start")
    if not isinstance(stop, int):
        raise TypeError("input must be a long stop")
    if not isinstance(step, int):
        raise TypeError("input must be a long step")
    while start < stop:
        yield start
        start += step
    raise StopIteration()


for i in arange(0, 20, 2):
    print(i)
