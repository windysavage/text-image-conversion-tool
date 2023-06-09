build:
	docker build -t lugia .

shell:
	docker run -it --rm lugia bash

local-web-start:
	docker run -d -p 8000:8000 --name pybase --mount type=bind,source=${PWD},target=/app lugia gunicorn --bind :8000 --workers 1 lugia.wsgi

local-web-stop:
	docker container rm pybase -f

local-deploy:
	gunicorn --bind 127.0.0.1:8000 --workers 1 lugia.wsgi

test:
	python -m pytest tests -vv
