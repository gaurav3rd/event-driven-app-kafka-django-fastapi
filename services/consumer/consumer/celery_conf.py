import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "consumer.settings")

app = Celery("consumer")

# app.config_from_object("celeryconfig")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "Populate new todos every minute": {
        "task": "todo.tasks.populate_todos",
        "schedule": crontab(minute=1),
    }
}
