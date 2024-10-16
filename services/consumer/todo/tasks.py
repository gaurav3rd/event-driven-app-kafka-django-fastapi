import logging
from celery import shared_task

from config import get_kafka_consumer
from .models import Todo


logging.basicConfig(level=logging.DEBUG)


@shared_task
def populate_todos():
    logging.info("started populate_todos")

    consumer = get_kafka_consumer(topic="todo-create")

    logging.info("started polling new todos")
    new_todos = consumer.poll(
        timeout_ms=10000, max_records=5000
    )  # long polling of 10 seconds

    if not new_todos:
        return

    todos = []
    for records in new_todos.values():
        for todo in records:
            todos.append(
                Todo(
                    title=todo.value.get("title", ""),
                    description=todo.value.get("description", ""),
                )
            )
    try:
        Todo.objects.bulk_create(todos)

    except Exception as e:
        logging.error(f"Error while bulk creating todos: {e}")
    logging.info("[COMPLETE] completedpopulate_todos")
