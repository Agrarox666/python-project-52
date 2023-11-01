install:
	poetry install

build:
	./build.sh

dev:
	poetry run flask --app page_analyzer:app run

lint:
	poetry run flake8 page_analyzer

local:
	poetry run gunicorn -w 5 -b 0.0.0.0:8500 page_analyzer:app

start:
	python manage.py runserver