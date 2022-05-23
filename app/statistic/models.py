""" statistics models """

from django.db import models
from users.models import UserProfile
from game.models import Collectable

# Create your models here.

class Rating(models.Model):
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    id_rating = models.IntegerField(primary_key=True)
    puzle = models.CharField(max_length=255)
    collectable = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    misions = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    

class MatchScore(models.Model):
    id_split_score = models.IntegerField(primary_key=True)
    id_rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    split_score = models.CharField(max_length=255)

class UserScore(models.Model):
    id_user_score = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    id_collectable = models.ForeignKey(Collectable, on_delete=models.CASCADE)
    match_score = models.ForeignKey(MatchScore, on_delete=models.CASCADE)
    user_score = models.CharField(max_length=255)
    
    
    