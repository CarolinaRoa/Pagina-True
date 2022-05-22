"""  User models  """
from django.db import models
from django import forms


# Create your models here.

class User(models.Model):
    """ Profile Model """
    #user = models.In(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank= False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    user_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    password = forms.CharField(widget=forms.PasswordInput())
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """ return username """
        return self.user_name
    