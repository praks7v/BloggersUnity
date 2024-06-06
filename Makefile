# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Used by `image`, `push` & `deploy` targets, override as required
IMAGE_REG ?= localhost:5000
IMAGE_REPO ?= bloggersunity
IMAGE_TAG ?= latest

# Project directory
PROJECT_DIR = BloggersUnity

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
	@echo "	 make image        - Build the Docker image"
	@echo "  make push         - Push image to the registry"
	@echo "  make lint         - Run linters (flake8 and pylint)"
	@echo "  make format       - Format code using black"

# Create virtual environment
venv:
	python3 -m venv $(VENV)

# Install dependencies
install: venv
	$(PIP) install -r requirements.txt

# Run linters
lint: venv
	$(VENV)/bin/flake8 $(PROJECT_DIR)


# Format code
format: venv
	$(VENV)/bin/black $(PROJECT_DIR)

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


image:  ## 🔨 Build container image from Dockerfile 
	docker build . --file build/Dockerfile \
	--tag $(IMAGE_REG)/$(IMAGE_REPO):$(IMAGE_TAG)

push:  ## 📤 Push container image to registry 
	docker push $(IMAGE_REG)/$(IMAGE_REPO):$(IMAGE_TAG)

# Clean the project
clean:
	-find . -name "*.pyc" -exec rm -f {} +
	-find . -name "*.pyo" -exec rm -f {} +
	-find . -name "__pycache__" -exec rm -rf {} + || true
	@if [ -d "$(VENV)" ]; then rm -rf $(VENV); fi

.PHONY: help venv install run migrate makemigrations test clean
