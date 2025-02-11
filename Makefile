.DEFAULT_GOAL := test

build:
	poetry build

clean:
	-rm -rf dist/

install:
	poetry install --all-groups
	poetry run pre-commit install

install_ci:
	poetry sync

test:
	poetry run ruff check py_utils
	poetry run ruff format --check --diff py_utils
