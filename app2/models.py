from django import forms
from django.db import models
from django.utils.timezone import datetime


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    weight = models.FloatField()
    price = models.FloatField()
    created_at= models.TimeField(default=datetime.now)
    updated_at = models.TimeField(default=datetime.now)



    def __str__(self):
        return self.name
