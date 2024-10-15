import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "consumer.settings")

app = Celery("consumer")

# app.config_from_object("celeryconfig")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
