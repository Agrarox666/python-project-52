#!/usr/bin/env bash

set -o errexit

poetry install
python3 manage.py migrate