broker_url = "redis://redis:6379/"
timezone = "Asia/Kathmandu"
beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"
result_extended = True
result_backend = broker_url
