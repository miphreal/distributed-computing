import celery


@celery.task(name='ic.mapper')
def mapper():
    #split your problem in embarrassingly parallel maps
    maps = [map.s(), map.s(), map.s(), map.s(), map.s(), map.s(), map.s(), map.s()]
    #and put them in a chord that executes them in parallel and after they finish calls 'reduce'
    mapreduce = celery.chord(maps)(reduce.s())
    return "{0} mapper ran on {1}".format(celery.current_task.request.id, celery.current_task.request.hostname)


@celery.task(name='ic.map')
def map():
    #do something useful here
    import time
    time.sleep(10.0)
    return "{0} map ran on {1}".format(celery.current_task.request.id, celery.current_task.request.hostname)


@celery.task(name='ic.reduce')
def reduce(results):
    #put the maps together and do something with the results
    return "{0} reduce ran on {1}".format(celery.current_task.request.id, celery.current_task.request.hostname)
