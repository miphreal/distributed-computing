# coding=utf-8
from __future__ import unicode_literals
from collections import Counter, defaultdict

from celery import chord
from celery.task import task
from funcy import ichunks, icat, take, walk_values
import nltk
#nltk.download('all', quiet=True)


@task(name='ex2.mapper')
def mapper(text='gatsby'):
    """Splits a problem into a number of small tasks"""
    import os
    fname = os.path.join(os.path.dirname(__file__), 'map_reduce2-{text}.txt'.format(text=text))
    with open(fname, 'r') as f:
        paralleled_problem = []
        for c in ichunks(50, f):
            paralleled_problem.append(m.s(' '.join(map(lambda t: t.decode('utf-8'), c))))
    return (chord(paralleled_problem, g.s() | r.s())).delay()


@task(name='ex2.grouping')
def g(stats):
    aggregated_stats = defaultdict(list)
    for word, count in icat(stats):
        aggregated_stats[word].append(count)

    return aggregated_stats.items()


@task(name='ex2.map')
def m(text):
    """Small task: returns a hash map"""
    tokens = nltk.word_tokenize(text)
    tokens = map(lambda w: w.strip('“”,.!?;:$&^*()…„``\'-').lower(), tokens)
    tokens = filter(bool, tokens)
    stats = Counter(tokens)
    return stats.items()


@task(name='ex2.reduce')
def r(stats):
    """Reduce collection of results"""
    sorted_stats = reversed(sorted(walk_values(sum, stats), key=lambda s: s[1]))

    return {
        'words': len(stats),
        'top': list(sorted_stats),
    }
