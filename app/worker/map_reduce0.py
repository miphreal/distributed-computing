# coding=utf-8
from __future__ import unicode_literals
from celery.task import task
import celery


@task(name='ex0.mapper')
def mapper():
    """Splits a problem into a number of small tasks"""
    paralleled_problem = map(m.s, range(10000))
    map_reduce = celery.chord(paralleled_problem)(r.s())
    return map_reduce


@task(name='ex0.map')
def m(x):
    """Small task"""
    return x ** x


@task(name='ex0.reduce')
def r(results):
    """Aggregates result"""
    return {'sum x^x, x=[0..10000)': sum(results)}
