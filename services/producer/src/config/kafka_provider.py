import json

from kafka import KafkaProducer


def get_producer() -> KafkaProducer:
    """
    Get a Kafka producer instance.

    Returns:
        KafkaProducer: A Kafka producer instance.
    """
    return KafkaProducer(
        bootstrap_servers=["kafka:9093"],
        retries=2,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )  # using the INSIDE config of KAFKA_ADVERTISED_LISTENERS


def send_to_topic(topic: str, body: dict) -> bool:
    """
    Send a message to a Kafka topic.

    Args:
        topic (str): The Kafka topic to send the message to.
        body (dict): The message body to send.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    # with get_producer() as producer:
    #     try:
    #         producer.send(topic, body)

    #     except Exception:
    #         return False
    # return True

    producer = get_producer()

    try:
        producer.send(topic, body)
        producer.flush()

    except Exception as e:
        # print(f"======> {e}")
        return False

    return True
