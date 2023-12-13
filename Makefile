install:
	poetry install
	python manage.py makemigrations
	python manage.py migrate

lint:
	poetry run flake8

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application
