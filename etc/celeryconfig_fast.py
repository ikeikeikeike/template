# -*- coding: utf-8 -*-
from celeryconfig import *
from kombu import Queue


# 起動用のQueue - Set boot queue
CELERY_QUEUES = (
    Queue("fast", ),
)


""" Queue受信設定

どのCeleryでレシーブするか設定出来るみたい


.. note:: 何度も試したが上手く出来た試しがない


**下記と同等の処理が可能らしい**

::

    from celery import task

    # 引数を指定しなくてもレシーバーの設定が可能
    # e.p.) @task(queue="fast")
    #
    @task
    def fast():
        return "fast"

"""
# CELERY_ROUTES = {
    # "fast.tasks.fast": {"queue": "fast"},
# }


# Email address used as sender (From field).
SERVER_EMAIL = "no-reply-celery-fast@bizmobile.co.jp"
