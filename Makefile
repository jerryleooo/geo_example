.PHONY: clean install help test run dependencies

help:
	@echo "  clean              remove unwanted stuff"
	@echo "  install            install geo_example and setup"
	@echo "  tests              run the testsuite"
	@echo "  run                run the development server"

dependencies:requirements.txt
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

unittest:
	py.test --cov=geo_example --cov-report=term-missing tests/unittests -vv

apitest:
	py.test --cov=geo_example --cov-report=term-missing tests/apitests -vv

test:
	py.test --cov=geo_example --cov-report=term-missing tests -vv

run:
	python manage.py runserver -dr

install:dependencies
	clear
	python manage.py install

routes:
	python manage.py list_routes

