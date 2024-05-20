import os
from dotenv import load_dotenv
from celery import Celery
from django.conf import settings

# Load environment variables from .env
load_dotenv()

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Create a Celery instance
app = Celery('backend')

# Configure Celery using Django settings
app.config_from_object('django.conf:settings', namespace="CELERY")

# Auto-discover tasks in your Django app
app.autodiscover_tasks()
