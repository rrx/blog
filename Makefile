.PHONY: default install build fmt

default:

install:
	python -m pip install -r requirements-dev.txt

build:
	npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css
	python -m builder

watch-css:
	npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
watch-html:
	python -m builder serve
watch:
	npx concurrently "make watch-css" "make watch-html"

fmt:
	isort .
	black .
