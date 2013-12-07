# coding=utf-8
from __future__ import unicode_literals
from cmd import Cmd
from celery import Celery

import config


app = Celery()
app.config_from_object(config)
app.loader.import_default_modules()


class Client(Cmd):
    intro = "Distributed computing.\nBSUIR 2013, Evgeny Lychkovsky\n"
    prompt = 'exec> '

    def do_tasks(self, _):
        chapter = ''
        for t, func in sorted(((t, f) for t, f in app.tasks.items() if not t.startswith('celery'))):
            task_chapter = t.partition('.')[0]
            if task_chapter != chapter:
                print '{:=^40}'.format(task_chapter)
                chapter = task_chapter
            doc = func.__doc__ or ''
            print '* {:<40} : {}'.format(t, doc.strip())

    def do_ex1(self, _):
        from worker.map_reduce import mapper
        r = mapper.delay()
        r = r.get()
        print(r.get())


if __name__ == '__main__':
    Client().cmdloop()
