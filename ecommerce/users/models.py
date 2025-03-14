from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_seller = models.BooleanField(default=False)  # Si el usuario es vendedor o no

    def __str__(self):
        return self.username
