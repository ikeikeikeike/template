# -*- coding: utf-8 -*-
from settings_devel import *
import djcelery


# loader
djcelery.setup_loader()


# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True


# overwrite ADMINS
ADMINS = (
    ('BizMobile Ops', 'ops@bizmobile.co.jp'),
    ("Tatsuo Ikeda", "tatsuo.ikeda@beproud.jp"),
)

# Email address used as sender (From field).
SERVER_EMAIL = "no-reply-celery@bizmobile.co.jp"


# 秒間の処理上限
CELERY_ANNOTATIONS = {"*": {"rate_limit": "1000/s"}}


# Name of the pool class used by the worker. - processes(default), eventlet, gevent.
CELERYD_POOL = "eventlet"


""" 起動プロセス数

* processes
  - Number of Unix process.

* eventlet
  - Number of micro thread.

* gevent
  - Number of micro thread.

"""
CELERYD_CONCURRENCY = 2000


# モニタリング用 リザルト出力
CELERY_SEND_EVENTS = True


# ログレベル - Can be one of DEBUG, INFO, WARNING, ERROR or CRITICAL.
CELERY_REDIRECT_STDOUTS_LEVEL = "DEBUG"
