install:
	poetry install

build:
	./build.sh

lint:
	poetry run flake8 page_analyzer

start:
	python manage.py runserver