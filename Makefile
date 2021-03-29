run-services:
	docker-compose up -d

run-api:
	./manage.py runserver

apply-migrations:
	./manage.py migrate

make-migrations:
	./manage.py makemigrations

freeze-dependencies:
	pip freeze > requirements.txt

drop-database:
	docker container rm -f poc-database
	docker volume rm django-authentication-poc_poc-database
	docker-compose up -d poc-database
