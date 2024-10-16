from celery import shared_task

from consumer.config import get_kafka_consumer
from todo.models import Todo


@shared_task
def populate_todos():
    consumer = get_kafka_consumer(topic="todo")

    new_todos = consumer.poll(
        timeout_ms=10000, max_records=5000
    )  # long polling of 10 seconds

    if not new_todos:
        return

    todos = [
        Todo(title=todo.value["title"], description=todo.value["description"])
        for todo in new_todos.values()
    ]

    try:
        Todo.objects.bulk_create(todos)

    except Exception as e:
        print(f"Failed to populate todos: {e}")
