from django.contrib.auth.models import AbstractUser


class Visitor(AbstractUser):

    def __str__(self):
        return self.username

