#!/usr/bin/env bash
set -e
echo "Running database migrations..."
python manage.py migrate
echo "Starting development server..."
python manage.py runserver 0.0.0.0:8000