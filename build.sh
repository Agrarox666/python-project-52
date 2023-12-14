#!/usr/bin/env bash

set -o errexit

poetry install && psql PGPASSWORD=DakNkMWU4tAY9dxFVKbNmKRuaa1yMdc2 psql -h dpg-clst94tcm5oc73bbmu90-a.oregon-postgres.render.com -U test_manager_db_user test_manager_db
python3 manage.py makemigrations
python3 manage.py migrate