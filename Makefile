dev:
	python3 manage.py runserver
install:
	poetry install --no-root
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) diplom.wsgi