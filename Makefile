install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 gendiff

check:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff