from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_time = models.DateTimeField(default=timezone.now)


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
