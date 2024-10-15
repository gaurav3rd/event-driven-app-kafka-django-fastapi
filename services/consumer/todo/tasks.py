from celery import shared_task


@shared_task
def populate_todos():
    # Task logic here
    print("This is a cron job running...")
