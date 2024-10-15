#!/bin/bash

echo "initializing container..."
python manage.py runserver 0.0.0.0:20001

python manage.py makemigrations --noinput
python manage.py migrate --noinput

DJNGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME} \
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD} \
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL} \
python manage.py createsuperuser --noinput

trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM

echo "finished successfully"
