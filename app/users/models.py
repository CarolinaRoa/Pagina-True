"""  User models  """

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    """ Profile Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #user_name = models.CharField(max_length=255, blank=False, null=False)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """ return username """
        return self.user.username
    