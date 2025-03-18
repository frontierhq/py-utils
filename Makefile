.DEFAULT_GOAL := test

build:
	uv build

clean:
	-rm -rf dist/

install:
ifeq ($(CI),true)
	uv sync --frozen
else
	uv sync
	uv run pre-commit install
endif

test:
	uv run ruff check py_utils
	uv run ruff format --check --diff py_utils
