from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Offer

##  Form to register user  ##
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


## Add the required fields to this Form from 'Offer' ##

class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['name', 'description', 'location', 'price', 'area', 'property_type']