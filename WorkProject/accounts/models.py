from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


###


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
            return self.role


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    role_id = models.CharField(max_length=50)
