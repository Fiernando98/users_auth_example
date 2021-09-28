from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxValueValidator
from django.db import models

from apps.user.models import User


class CustomProfile(models.Model):
    user = models.OneToOneField(to=User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username
