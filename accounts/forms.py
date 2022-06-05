from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from . import models


class OrderForm(ModelForm):
    
    class Meta:
        model = models.Order
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginUserForm(AuthenticationForm):
    
    pass


    

