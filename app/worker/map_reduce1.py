# coding=utf-8
from __future__ import unicode_literals
import random
import time

from celery import chord
from celery.task import task


@task(name='ex1.mapper')
def mapper():
    """Splits a problem into a number of small tasks"""
    rnd_data = lambda: random.sample(xrange(1000000000), 100)
    paralleled_problem = map(lambda v: m.s(rnd_data()), xrange(1000))
    return (chord(paralleled_problem, g.s() | r.s())).delay()


@task(name='ex1.grouping')
def g(maps):
    gr = {
        'sum': [],
        'exp': [],
        'avg': [],
        'func': [],
    }

    for data in maps:
        for name in ('sum', 'exp', 'avg', 'func'):
            if name in data:
                gr[name].append(data[name])
    return gr


def _avg(values):
    if values:
        v = list(values)
        return sum(v) / len(v)


@task(name='ex1.map')
def m(values):
    """Small task: returns a hash map"""
    x1sum = sum(values)
    x2exp = _avg(map(lambda v: x1sum / v, values))
    x3avg = _avg(values)
    func = x1sum * x3avg * x2exp

    # emulate heavy work
    time.sleep(2)  # that takes 2 sec at least

    return {
        'sum': x1sum,
        'exp': x2exp,
        'avg': x3avg,
        'func': func,
    }


@task(name='ex1.reduce')
def r(map_results):
    """Reduce collection of results"""
    return {
        'sum': _avg(map_results.get('sum', ())),
        'avg_exp': _avg(map_results.get('exp', ())),
        'avg_avg': _avg(map_results.get('avg', ())),
        'avg_func': _avg(map_results.get('func', ())),
    }
