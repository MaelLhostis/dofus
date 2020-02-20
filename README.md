# dofus

## Install dependencies

bash:
'''
sudo apt install python3 python3-venv python3-dev python3-pip libpq-dev postgresql postgresql-contrib
'''

## Create Database

bash:
'''
sudo su - postgres
psql
'''

SQL commands:
'''
CREATE DATABASE djangoddofus;

CREATE USER admin WITH PASSWORD 'admin';

ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE djangoddofus TO admin;

\q
'''

bash:
'''
exit
'''

## Create virtual environment

bash into main folder:
'''
python3 -m venv .venv
source .venv/bin/activate
'''

bash into django main folder, venv activated:
'''
pip3 install -r requirements.txt
'''

## Migrate Database

bash into django main folder, venv activated:
'''
python3 manage.py makemigrations
python3 manage.py migrate
'''

## Create SuperUser

bash into django main folder, venv activated:
'''
python3 manage.py createsuperuser
'''

## Launch App

bash into django main folder, venv activated:
'''
python3 manage.py runserver
'''
