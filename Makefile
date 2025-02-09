dev:
	python3 manage.py runserver
build:
	poetry install
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) diplom.wsgi