from django.db import models


# Create your models here.

class GithubUser(models.Model):
    login = models.CharField(max_length=50)
    id = models.IntegerField()
    avatar_url = models.TextField()
    score = models.FloatField()