CELERYD_CONCURRENCY = 8
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Europe/Minsk'
BROKER_URL = 'amqp://guest@mq1:5672/'
CELERY_ACCEPT_CONTENT = ['json', 'pickle', 'msgpack', 'yaml']
