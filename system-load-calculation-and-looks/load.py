#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import exp
import numpy as np


def _update_load(load, task_counts, load_period, update_period=5):
    """
    Formula from article
        Load和CPU利用率是如何算出来的
        http://www.penglixun.com/tech/system/how_to_calc_load_cpu.html

        load1  = load1  * exp(-5 / 60)  + n * (1 - exp(-5 / 60))
        load5  = load5  * exp(-5 / 300) + n * (1 - exp(-5 / 300))
        load15 = load15 * exp(-5 / 900) + n * (1 - exp(-5 / 900))

        :param load_period seconds
        :param update_period seconds, default 5 secs
    """
    beta = exp(-update_period / load_period)
    # Exponential moving average
    # https://en.wikipedia.org/wiki/Moving_average
    alpha = 1 - beta
    return task_counts * alpha + load * (1 - alpha)


def loads(task_count, load_period, update_period=5):
    load = 0
    ret = np.zeros(len(task_count))

    for idx, n in enumerate(task_count[:-1]):
        load = _update_load(load, task_count[idx], load_period, update_period)
        ret[idx + 1] = load

    return ret


def load1s(task_count):
    return loads(task_count, 60)


def load5s(task_count):
    return loads(task_count, 60 * 5)


def load15s(task_count):
    return loads(task_count, 60 * 15)
