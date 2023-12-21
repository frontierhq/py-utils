clean:
	rm -rf build dist *.egg-info

install:
	pipenv install --dev
	pipenv run pre-commit install

install_ci:
	pipenv sync

release:
	pipenv run python setup.py sdist
	pipenv run twine upload dist/*

test:
	pipenv run flake8 py-utils
