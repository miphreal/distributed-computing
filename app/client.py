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

    def run(self, task, *args):
        return app.tasks[task].delay(*args).get()

    def do_run(self, task):
        print(self.run(task))

    def do_ex0(self, l):
        print 'Simple [mapper*map -> reduce]'
        print self.run('ex0.mapper').get()

    def do_ex1(self, l):
        print 'Simple [mapper*map -> group -> reduce]'
        print self.run('ex1.mapper').get()

    def do_ex2(self, l):
        print 'Words statistic...'
        if not l:
            print 'choose "gatsby" or "war"'
            return
        res = self.run('ex2.mapper', l).get()
        print 'Words:', res['words']
        print '== TOP: =='
        for word, count in res['top'][:60]:
            print '{:<7} {}'.format(count, word)
        print '...' if len(res['top']) > 60 else ''

if __name__ == '__main__':
    Client().cmdloop()
