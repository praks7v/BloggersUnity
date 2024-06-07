# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Used by `image`, `push` & `deploy` targets, override as required
IMAGE_REG ?= localhost:5000
IMAGE_REPO ?= bloggersunity-web
IMAGE_TAG ?= latest

# Project directory
PROJECT_DIR = BloggersUnity
APP_DIR = Tech

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
	@echo "	 make image        - Build container image from Dockerfile"
	@echo "  make push         - Push container image to registry "
	@echo "  make lint         - Run linters (flake8)"
	@echo "  make format       - Format code using black"
	@echo "  make clean        - Clean up Project" 
	@echo "  make compose:build - Build the Docker images using Docker Compose"
	@echo "  make compose:up   - Run the container using Docker Compose"
	@echo "  make compose:down - Stop the container using Docker Compose"

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
	$(VENV)/bin/black $(PROJECT_DIR) $(APP_DIR)

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
	docker build . --file docker/Dockerfile \
	--tag $(IMAGE_REG)/$(IMAGE_REPO):$(IMAGE_TAG)

push:  ## 📤 Push container image to registry 
	docker push $(IMAGE_REG)/$(IMAGE_REPO):$(IMAGE_TAG)

# Build the Docker images using Docker Compose
compose:build: 
	docker compose -f docker/docker-compose.yaml build

# Run the container using Docker Compose
compose:up:
	docker compose -f docker/docker-compose.yaml up -d

# Stop the container using Docker Compose
compose:down:
	docker compose -f docker/docker-compose.yaml down

# Clean the project
clean:
	-find . -name "*.pyc" -exec rm -f {} +
	-find . -name "*.pyo" -exec rm -f {} +
	-find . -name "__pycache__" -exec rm -rf {} + || true
	@if [ -d "$(VENV)" ]; then rm -rf $(VENV); fi

.PHONY: help venv install run migrate makemigrations test clean compose:build compose:up compose:down
