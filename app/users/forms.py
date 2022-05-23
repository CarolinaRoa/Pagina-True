""" forms from django """

from django import forms
from django.forms import ModelForm
from .models import UserProfile


class CustomUserCreationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'user_name', 'email', 'password']
        #fields = '__all__'
        
