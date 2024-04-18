import celery
import os
app = celery.Celery('example',broker='redis://localhost:6379')


@app.task
def add(x, y):
    return x + y