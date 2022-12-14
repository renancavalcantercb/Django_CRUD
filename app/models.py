from django.db import models


# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
