from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
import json
from .models import GitHubUser
from rest_framework.response import Response
from .serializers import GitHubUserSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def search_user(request):
    try:
        url = 'https://api.github.com/search/users'
        search = request.GET['q']
        GET_DATA = {'q': search}
        r = requests.get(url, params=GET_DATA)
        data = json.loads(r.text)
        users = data["items"]
        for user in users:
            try:
                u = GitHubUser.objects.get(login=user['login'])
                u.gid = user['id']
                u.avatar_url = user['avatar_url']
                u.score = user['score']
                u.save()
            except GitHubUser.DoesNotExist:
                u = GitHubUser.objects.create(login=user['login'],
                                              gid=user['id'],
                                              avatar_url=user['avatar_url'],
                                              score=user['score'])
                u.save()
        results = GitHubUser.objects.filter(login__contains=search)

        print(results)
        serializer = GitHubUserSerializer(results,
                                          many=True)

        return Response(serializer.data)
    except MultiValueDictKeyError:
        return HttpResponse("Error!! No search data")   
