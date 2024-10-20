# Implementation of Event Driven Architecture (in Microservice)

## Motivation

The goal of this project is to implement an **Event-Driven Architecture** in a microservice environment to achieve **high availability** under high traffic workloads. By decoupling services and relying on asynchronous communication via Kafka, the architecture ensures scalability, fault tolerance, and smooth handling of high loads.

## Basic Idea

The project consists of two primary services:
- A **FastAPI producer service** responsible for sending new todos to Kafka topics.
- A **Django consumer service** that consumes those todos from Kafka, and saves to database.

>The services are designed to operate _independently_ hence, both of these services can be scaled independently.

---
### Event-Driven Flow

1. **Producer Service (FastAPI)**:
   - Listens for HTTP requests and publishes messages to Kafka topics when user creates new todos.

2. **Broker (Kafka)**:
   - Acts as an intermediary to queue and distribute messages between producer and consumer services.

3. **Consumer Service (Django)**:
   - Listens to Kafka topics, fethes unprocessed todos, and stores data in a Postgres database (using bulk create).

4. **Celery with Redis**:
   - **Celery** is used to handle background tasks. It pulls the todos from Kafka topics periodically.
   - **Redis** acts as the **message broker** for Celery, ensuring tasks are distributed and executed efficiently in the background.
   - **Celery beat** is used to run cron jobs (to pull new todos)

## Tools & Technologies

- **FastAPI**
- **Kafka**
- **Django**
- **Celery** and **Celery beats**
- **Redis**
- **Postgres**

---

## STEPS TO START THE PROJECT:
1. Clone the project
2. Navigate to the **consumer/** directory
3. Create a new .env file (copy from .env.example) and fill in the environment variables
4. Navigate to the project root directory. Make sure you are in the same directory where **start_project.sh** file is located
5. Make the **start_project.sh** file executable by executing the following command:
```bash
chmod +x start_project.sh
```
6. Building the project
```bash
./start_project.sh --build
```
7. Start the project
```bash
./start_project.sh
```

---
## Create a new todo:
#### POST: http://localhost:7007/new/
**Example:**
```
curl --location 'localhost:7007/new/' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Do homework",
    "description": "Finish pending homeworks"
}'
```

### List todos:
#### GET: http://localhost:7008/api/todos/
