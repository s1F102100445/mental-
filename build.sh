#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install requests
pip install openai

python manage.py collectstatic --no-input
python manage.py migrate