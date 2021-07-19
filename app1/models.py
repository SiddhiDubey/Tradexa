from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Create your models here.

class User(models.Model):
   first_name = models.CharField(max_length=200, null=True)
   last_name = models.CharField(max_length=200, null=True)
   Email = models.CharField(max_length=200, null=True)
   password = models.CharField(max_length=200, null=True)
   username = models.CharField(max_length=200, null=True)


   def __str__(self):
       return self.first_name



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length=200, null=True)
    created_at = models.TimeField(default=datetime.now)
    updated_at = models.TimeField(default=datetime.now)


    def __str__(self):
        return str(self.text)


