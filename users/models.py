from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='first name')
    last_name = models.CharField(max_length=80, blank=True, null=True, verbose_name='last name')
    comment = models.TextField(blank=True, null=True, verbose_name='comment')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []