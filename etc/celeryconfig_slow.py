# -*- coding: utf-8 -*-
from celeryconfig import *
from kombu import Queue


# 起動用のQueue - Set boot queue
CELERY_QUEUES = (
    Queue("slow", ),
)


""" Queue受信設定

どのCeleryでレシーブするか設定出来るみたい


.. note:: 何度も試したが上手く出来た試しがない


**下記と同等の処理が可能らしい**

::

    from celery import task

    # 引数を指定しなくてもレシーバーの設定が可能
    # e.g.) @task(queue="slow")
    #
    @task
    def slow():
        return "fast"

"""
# CELERY_ROUTES = {
    # "slow.tasks.slow": {"queue": "slow"},
# }


# Email address used as sender (From field).
SERVER_EMAIL = "no-reply-celery-slow@bizmobile.co.jp"
