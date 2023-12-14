#!/usr/bin/env bash

set -o errexit

poetry install && psql -a -d $DATABASE_URL
python3 manage.py makemigrations
python3 manage.py migrate