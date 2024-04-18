from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser
from . models import *





class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

        
