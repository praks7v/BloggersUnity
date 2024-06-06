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

  Clone the project to any directory where you do development work
  
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

5. **Usage**

Visit http://localhost:8000 to access the application.
Create an account and start writing your blog posts.

4. **Contributing**

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

5. **License**

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) - see the LICENSE file for details.

6. **Documentation**

For detailed documentation, see the BloggersUnity Documentation.

7. **Authors**

Prakash Satvi


8. **Screenshots**
Home
![Home Page](docs/source/_static/home_bloggersUnity.png)

Blog Post
![Blog Post](docs/source/_static/blog_posts.png)

Dashboard
![Dashboard](docs/source/_static/dashborad_bloggersunity.png)
