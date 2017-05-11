import datetime
from django.db import models


# Create your models here.

class GitHubUser(models.Model):
    login = models.CharField('login', max_length=50, unique=True)
    gid = models.IntegerField('id')
    avatar_url = models.TextField('avatar_url')
    score = models.FloatField('Score')
    date_added = models.DateField('Added On', default=datetime.datetime.now)

    def __str__(self):
        return self.login

    def avatar(self):
        return u'<img src="%s" width="30px" height="30px"/>' % self.avatar_url

    avatar.short_description = 'Thumbnail'
    avatar.allow_tags = True
