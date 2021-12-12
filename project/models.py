from django.db import models
from django.contrib.auth.models import AbstractUser

### Custom user model to login with email ###
class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)

    ### Change USERNAME_FIELD to 'username' instead of 'email' to avoid errors when creating super users with command manage.py createsuperuser ###
    ### Use 'email' to register/login with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


### This model will display property types ###
class LandType(models.Model):
    property_type = models.CharField(max_length=200)

    class Meta:
        ordering = ['-property_type']

    def __str__(self):
        return self.property_type


### These are the main fields to be used in FORMS when creating an offer. Note that not all have to be used ### 
class Offer(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    location = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    area = models.IntegerField(null=False)
    image = models.ImageField(null=True, default="farm-5836815_1920.jpg")
    created = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    property_type = models.ForeignKey(LandType, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-views']

    def __str__(self):
        return self.name
