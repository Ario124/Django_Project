from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)

    ### Change USERNAME_FIELD to 'username' instead of 'email' to avoid errors when creating super users with command manage.py createsuperuser ###
    ### Use 'email' to register/login with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class LandType(models.Model):
    property_type = models.CharField(max_length=200)

    def __str__(self):
        return self.property_type

class Offer(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    location = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    area = models.IntegerField(null=False)
    property_type = models.ForeignKey(LandType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name






# class Offer(models.Model):
#     host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.name