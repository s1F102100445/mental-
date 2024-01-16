#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
sudo apt-get install portaudio19-dev
pip install pyaudio
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py superuser
