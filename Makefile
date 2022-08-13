export PATH := $(PWD)/.venv/bin:$(PATH)
export VIRTUAL_ENV := $(PWD)/.venv
export SRC_DIR := $(shell ls */main.py | xargs dirname)

COLOR="\033[36m%-30s\033[0m %s\n"
ENV_EXISTS=0

ERROR_MSG_DATABASE_URL="Define the variable DATABASE_URL=postgresql://<user>:<pass>@<host>:<port>/<db_name> in .env file"
ERROR_MSG_ENV_NOT_FOUND="Create .env file (touch .env) and define the variable DATABASE_URL=postgresql://<user>:<pass>@<host>:<port>/<db_name>"

.PHONY: .env .venv
.DEFAULT_GOAL := help

ifeq ($(wildcard .env), .env)
    include .env
    export $(shell sed 's/=.*//' .env)
    ENV_EXISTS=1
endif

.start-validation:
	@if [ $(ENV_EXISTS) -eq 0 ]; then echo $(ERROR_MSG_ENV_NOT_FOUND) && exit 1; fi
	@if [ ! $(shell grep DATABASE_URL .env) ]; then echo $(ERROR_MSG_DATABASE_URL) && exit 1; fi

.env-file:
	@echo 'PYTHONPATH="$(SRC_DIR)"' > .env

.venv:
	@python3.10 -m venv $(VIRTUAL_ENV)
	pip install --upgrade pip

.rm-venv:
	@if [ -d $(VIRTUAL_ENV) ]; then rm -rf $(VIRTUAL_ENV); fi

.install-hook:
	@echo "make lint" > .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit

install: .venv .env-file .install-hook  ## Create .venv and install dependencies.
	@if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

reinstall: .rm-venv install ## Remove .venv if exists, create a new .venv and install dependencies.

install-dev: install ## Create .venv and install dev dependencies.
	if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

reinstall-dev: .rm-venv install-dev ## Remove .venv if exists, create a new .venv and install dev dependencies.

clean: ## Clean all caches file.
	@rm -rf dependencies .pytest_cache .coverage
	@find $(PROJECT_PATH) -name __pycache__ | xargs rm -rf
	@find tests -name __pycache__ | xargs rm -rf

lint: ## Apply lintings to ensure code quality.
	black --line-length=100 --target-version=py38 --check .
	flake8 --max-line-length=150 --ignore=E402,W503 --exclude .venv,dependencies,fixtures,src/geobuf --max-complexity 5

format: ## Format code based in PEP8.
	black --line-length=100 --target-version=py38 .

coverage: ## Test code and check coverage from tests.
	@pytest --cov-config=.coveragerc --cov-report term-missing --cov=$(SRC_DIR) tests/ --cov-fail-under=90

test:  ## Execute all unity tests.
	@pytest -s

security: ## Run scripts for static security analysis
	@echo ">>> [Ochrona]"
	@ochrona -r requirements.txt

start: .start-validation ## Start API in local for development.
	@uvicorn $(SRC_DIR).main:app --root-path . --reload

help: ## Show documentation.
	@for makefile_file in $(MAKEFILE_LIST); do \
		grep -E '^[a-zA-Z_-]+:.*?##' $$makefile_file | sort | awk 'BEGIN {FS = ":.*?##"}; {printf ${COLOR}, $$1, $$2}'; \
	done
