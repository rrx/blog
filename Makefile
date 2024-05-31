.PHONY: default install build fmt

default:

install:
	python -m pip install -r requirements-dev.txt

build:
	npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css
	python -m builder

fmt:
	isort .
	black .
