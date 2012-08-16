import time
from celery import task


# @task
@task(queue="slow")
def slow():
    time.sleep(10)
    return "slow"
