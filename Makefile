install:
	sh ./build.sh

lint:
	poetry run flake8

tests:
	python manage.py test

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application
