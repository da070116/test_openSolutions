from django.db import models
from django.contrib.auth.models import AbstractUser


class Visitor(AbstractUser):
    name = models.CharField(blank=True, max_length=125)

    def __str__(self):
        return self.username

# https://pythondigest.ru/view/34325/
# https://djangochannel.com/blog/django/django_rest_framework_autentifikatsii_polzovatelej-337/


