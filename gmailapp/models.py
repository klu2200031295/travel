from django.db import models

# Create your models here.
from django.apps import AppConfig


class GmailappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gmailapp'