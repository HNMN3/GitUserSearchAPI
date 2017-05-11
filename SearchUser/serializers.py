# Keep coding and change the world..And do not forget anything..Not Again..
from rest_framework import serializers
from .models import GitHubUser


class GitHubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubUser
        fields = '__all__'


