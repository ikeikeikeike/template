from celery import task


@task()
def normal():
    return "normal"
