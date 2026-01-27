.PHONY: fail-if-no-virtualenv all install loaddata test

all: install migrate loaddata collectstatic

install: fail-if-no-virtualenv
	pip install --pre --editable .[dev,test] --upgrade --upgrade-strategy=eager

migrate:
	sandbox/manage.py migrate --no-input

collectstatic:
	sandbox/manage.py collectstatic --no-input

lint:
	flake8 oscar_invoices tests sandbox setup.py
	isort -c -q --diff oscar_invoices/ sandbox/ tests/

test: install
	PYTHONPATH=. pytest

clean: ## Remove files not in source control
	find . -type f -name "*.pyc" -delete
	rm -rf nosetests.xml coverage.xml htmlcov *.egg-info *.pdf dist violations.txt

package: clean
	pip install --upgrade pip twine wheel
	rm -rf dist/
	rm -rf build/
	python setup.py clean --all
	python setup.py sdist bdist_wheel

release: package ## Creates release
	twine upload -s dist/*
