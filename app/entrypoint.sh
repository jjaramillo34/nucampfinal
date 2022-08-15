#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database makemigrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8083
# Start server
#echo "Starting server"
#waitress-serve --port=$PORT mysite.wsgi:application