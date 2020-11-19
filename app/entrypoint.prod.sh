#!/bin/sh
# 需要手动执行migrate
# docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"