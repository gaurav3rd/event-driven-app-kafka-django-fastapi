import json
from kafka import KafkaConsumer


def get_kafka_consumer(topic: str, **kwargs) -> KafkaConsumer:
    """
    Get a Kafka consumer instance.

    Returns:
        KafkaConsumer: A Kafka consumer instance.
    """
    return KafkaConsumer(
        topic,
        bootstrap_servers=["kafka:9093"],
        auto_offset_reset="earliest",
        group_id="todo",
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        **kwargs
    )
