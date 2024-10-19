#!/bin/bash
CONSUMER_PATH="services/consumer/docker-compose.yml"
PRODUCER_PATH="services/producer/docker-compose.yml"


build_images (){
    echo "building producer...";
    docker compose -f ${CONSUMER_PATH} down
    docker compose -f ${CONSUMER_PATH} build -d --no-cache

    echo "building consumer...";
    docker compose -f ${PRODUCER_PATH} down
    docker compose -f ${PRODUCER_PATH} up -d --no-cache

}

run_containers (){
    echo "starting kafka...";
    docker compose -f docker-compose-kafka.yml up -d

    echo "starting producer...";
    docker compose -f services/producer/docker-compose.yml up -d

    echo "starting consumer...";
    docker compose -f services/consumer/docker-compose.yml up -d

}

if [[ "$1" == "--build" ]]; then
    build_images
fi


run_containers

trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM

echo "[FINISHED] Running all containers..."
