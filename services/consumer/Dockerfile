FROM python:3.10

ENV CONTAINERUSER=microservice
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER root

WORKDIR /app

COPY . /app

RUN apt update && apt install -y git build-essential libpq-dev --no-install-recommends \
    && python -m pip install --upgrade pip \
    && pip install -r ./requirements.txt \
    && apt-get clean \
    && mkdir -p /app \
    && useradd -m ${CONTAINERUSER} \
    && chown -R ${CONTAINERUSER}: /app \
    && chmod +x ./.scripts/start.sh

USER ${CONTAINERUSER}

# ENV PATH="/home/${CONTAINERUSER}/.local/bin:$PATH"

EXPOSE 20001

ENTRYPOINT [ "./.scripts/start.sh" ]