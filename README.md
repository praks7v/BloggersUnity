# BloggersUnity

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

BloggersUnity is a web application that allows users to create and publish blog posts. It's built with [Django](https://www.djangoproject.com/) 
and offers features like user authentication, creating, editing, and deleting posts.

## Features

- User authentication (signup, login, and logout)
- Create and publish blog posts
- Edit and delete your own posts
- View and browse posts by category
- User profile with avatar and contact information
- ...


## Getting Started

These instructions will help you set up a local development environment.

1. **Prerequisites**
   - Be using Linux, WSL or MacOS, with bash, make etc.
   - Python 3.x - for running locally, linting, running tests etc.
   - ...

2. **Installation**

   Clone the project to any directory where you do development work.
  
   ```bash
   git clone https://github.com/praks7v/BloggersUnity.git
   ```
   ```bash
   cd BloggersUnity
   make venv
   make install
   make makemigrations
   make migrate
   make run
   ```
3. **Makefile**

   A standard GNU Make file is provided to help with running and building locally.
   ```
     make help         - This is for help
     make venv         - Create a virtual environment
     make install      - Install dependencies
     make run          - Run the Django development server
     make migrate      - Apply database migrations
     make makemigrations - Create new database migrations
     make test         - Run tests
	  make image        - Build the Docker image
     make push         - Push image to the registry
     make lint         - Run linters (flake8)
     make format       - Format code using black
     make clean        - Clean up Project
   ```
   Make file variables and default values, pass these in when calling `make`, e.g. `make image IMAGE_REPO=blah/foo`

   | Makefile Variable | Default                |
   | ----------------- | ---------------------- |
   | IMAGE_REG         | docker<span>.</span>io |
   | IMAGE_REPO        | username/project_name  |
   | IMAGE_TAG         | latest                 |


   The app runs under Django and listens on port 8000 by default, this can be changed with the `PORT` environmental variable.

### Usage

   Visit http://localhost:8000 to access the application.
   Create an account and start writing your blog posts.

### Contributing

   Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.
   
### License
   This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) - see the LICENSE file for details.

### Documentation

   For detailed documentation, see the BloggersUnity Documentation.

### Authors
   
   [Praks7v](https://github.com/praks7v)


### Screenshots
Home
![Home Page](docs/source/_static/home_bloggersUnity.png)

Blog Post
![Blog Post](docs/source/_static/blog_posts.png)

Dashboard
![Dashboard](docs/source/_static/dashborad_bloggersunity.png)
