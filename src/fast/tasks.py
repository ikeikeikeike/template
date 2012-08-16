from celery import task


# @task
@task(queue="fast")
def fast():
    return "fast"
