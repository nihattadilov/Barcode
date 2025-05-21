#!/bin/bash

echo "🔄 Running migrate..."
python manage.py migrate

echo "🧹 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Gunicorn server..."
gunicorn Barcode.wsgi:application --bind 0.0.0.0:${PORT:-8000}
