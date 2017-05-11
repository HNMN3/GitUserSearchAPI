from django.db import models


# Create your models here.

class GitHubUser(models.Model):
    login = models.CharField('login', max_length=50, unique=True)
    gid = models.IntegerField('id')
    avatar_url = models.TextField('avatar_url')
    score = models.FloatField('Score')

    def __str__(self):
        return self.login