build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install

package-install:
	python -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

lint:
	poetry run flake8 page_loader

install-requirements:
	python -m pip install --user --upgrade pip
	python -m pip install poetry

test:
	poetry run pytest -vv --cov=page_loader --cov-report xml tests/