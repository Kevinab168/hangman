from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Game(models.Model):
    winning_word = models.CharField(max_length=200)
    attempts_left = models.IntegerField(default=6, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    in_progress = models.BooleanField(default=True)


class Guess(models.Model):
    guess_value = models.CharField(max_length=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
