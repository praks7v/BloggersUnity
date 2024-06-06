# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Help message
help:
	@echo "Makefile for Django project"
	@echo "Available commands:"
	@echo "  make venv         - Create a virtual environment"
	@echo "  make install      - Install dependencies"
	@echo "  make run          - Run the Django development server"
	@echo "  make migrate      - Apply database migrations"
	@echo "  make makemigrations - Create new database migrations"
	@echo "  make test         - Run tests"

# Create virtual environment
venv:
	python3 -m venv $(VENV)

# Install dependencies
install: venv
	$(PIP) install -r requirements.txt

# Create new database migrations
makemigrations: venv
	$(PYTHON) manage.py makemigrations

# Apply database migrations
migrate: venv
	$(PYTHON) manage.py migrate

# Run tests
test: venv
	$(PYTHON) manage.py test

# Run the Django development server
run: venv
	$(PYTHON) manage.py runserver

# Clean the project
clean:
	-find . -name "*.pyc" -exec rm -f {} +
	-find . -name "*.pyo" -exec rm -f {} +
	-find . -name "__pycache__" -exec rm -rf {} + || true
	@if [ -d "$(VENV)" ]; then rm -rf $(VENV); fi

.PHONY: help venv install run migrate makemigrations test clean
