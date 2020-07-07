release: python manage.py migrate --noinput
web: gunicorn {{ project_name }}.wsgi:application --log-file -
