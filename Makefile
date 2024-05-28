default:

install:
	python -m pip install -r requirements-dev.txt

fmt:
	isort .
	black .
