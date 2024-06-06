import os
import sys
import django

# Add the path to your Django project directory (not the inner project directory) to sys.path
sys.path.insert(0, "C:/Users/praks/PycharmProjects/BloggersUnity/BloggersUnity")

# Set the environment variable for your Django project's settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "BloggersUnity.settings"

# Import your Django project settings
django.setup()

# Project information
project = "BloggersUnity"
copyright = "2023, Prakash Satvi"
author = "Prakash Satvi"
version = "0.0.1"
release = "0.0.1"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

# Templates and exclude patterns
templates_path = ["_templates"]
exclude_patterns = []


# Include the URL documentation module
autodoc_modules = {
    "BloggersUnity.urls": "URL Documentation for BloggersUnity",
    "Tech.urls": "URL Documentation for BloggersUnity Tech apps",
}

# Options for HTML output
html_theme = "bizstyle"
html_static_path = ["_static"]
