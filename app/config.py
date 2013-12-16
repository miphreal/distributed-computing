CELERYD_CONCURRENCY = 8
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Europe/Minsk'
BROKER_URL = 'amqp://rmq_user:rmq_pass@mq1:5672/app'
CELERY_ACCEPT_CONTENT = ['json', 'pickle', 'msgpack', 'yaml']
CELERY_IMPORTS = (
    'worker.map_reduce0',
    'worker.map_reduce1',
    'worker.map_reduce2',
)
CELERY_RESULT_BACKEND = 'redis://db1:6379/0'
CELERY_DEFAULT_QUEUE = 'tasks:queue'
