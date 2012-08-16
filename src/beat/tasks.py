from celery import task


@task()
def beat():
    return "beat"
