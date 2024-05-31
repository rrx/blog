.PHONY: default install build fmt

default:

install:
	python -m pip install -r requirements-dev.txt

build:
	python -m builder

fmt:
	isort .
	black .
