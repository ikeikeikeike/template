# -*- coding: utf-8 -*-
from celeryconfig import *
from kombu import Queue


# �N���p��Queue - Set boot queue
CELERY_QUEUES = (
    Queue("fast", ),
)


""" Queue��M�ݒ�

�ǂ�Celery�Ń��V�[�u���邩�ݒ�o����݂���


.. note:: ���x������������肭�o�����������Ȃ�


**���L�Ɠ����̏������\�炵��**

::

    from celery import task

    # �������w�肵�Ȃ��Ă����V�[�o�[�̐ݒ肪�\
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
