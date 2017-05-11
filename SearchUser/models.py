from django.db import models


# Create your models here.

class GitHubUser(models.Model):
    login = models.CharField(max_length=50)
    id = models.IntegerField()
    avatar_url = models.TextField()
    score = models.FloatField()
