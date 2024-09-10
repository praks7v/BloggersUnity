#!/bin/bash
set -e

# Apply database migrations
echo "Applying database migrations"
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Start the Django server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
gunicorn myapp.wsgi:application --bind 0.0.0.0:8000

exec "$@"
