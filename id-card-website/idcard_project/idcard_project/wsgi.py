"""WSGI configuration for the idcard_project."""

import os
import sys

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(__file__))

# Set the settings module for the Django application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idcard_project.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()