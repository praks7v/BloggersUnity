#!/bin/bash
set -e

# Apply database migrations
echo "Applying database migrations"
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn"
gunicorn BloggersUnity.wsgi:application --bind 0.0.0.0:8000 --workers 3

exec "$@"
