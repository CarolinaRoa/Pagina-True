from django.db import models
from users.models import UserProfile

# Create your models here.
class Collectable(models.Model):
    id_collectable = models.IntegerField(primary_key=True)
    description = models.TextField()

class Match(models.Model):
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    id_match = models.IntegerField(primary_key=True)
    
class UserMatch(models.Model):
    id_user_match = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    id_match = models.ForeignKey(Match, on_delete=models.CASCADE)