from django.db.models.base import Model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Offer


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['name', 'description', 'location', 'price', 'area', 'property_type']