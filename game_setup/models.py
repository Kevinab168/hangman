from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
