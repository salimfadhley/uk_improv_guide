#!/usr/bin/env bash
set -e
./migrate.sh
echo "Starting development server..."
python manage.py runserver 0.0.0.0:8000