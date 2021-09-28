from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxValueValidator
from django.db import models


class User(models.Model):
    class UserType(models.IntegerChoices):
        SUPERUSER = 0
        MONITOR = 1
        RECRUITER = 2
        WORKER = 3

    username = models.CharField(unique=True, validators=[UnicodeUsernameValidator()], verbose_name='username',
                                max_length=50)
    email = models.EmailField(unique=True, verbose_name='email')
    account_type = models.IntegerField(choices=UserType.choices, default=None, null=False)

    def __str__(self):
        return self.username
