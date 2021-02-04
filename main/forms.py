from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Products,CartDetails
from django import forms

class UserData(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        