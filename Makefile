install:
	sh ./build.sh

install-prod:
	sh ./build-prod.sh

lint:
	poetry run flake8

tests:
	python manage.py test

test-coverage:
	@poetry run coverage run --source='.' manage.py test && poetry run coverage xml

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application
