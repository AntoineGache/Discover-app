# Discover-app
This is a social network to share musics and meet people

## Configuration

create a virtualenv:

* "virtualenv discover-app"
* On linux: "source ./discover-app/bin/activate"
* Install all packages: "pip install -r requirements.txt"
* To exit the virtualenv: "deactivate"

Launch the django server:

* python manage.py runserver

Launch databse: 

* Exécuter cette commande: "docker compose up -d"

Shutdown database:

* docker compose down

Database settings:

ip: localhost
user: root
password: root_password
port : 6000