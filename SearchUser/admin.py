from django.contrib import admin
from .models import GitHubUser


# Register your models here.

class GitHubUserAdmin(admin.ModelAdmin):
    list_display = ('gid', 'date_added', 'avatar', 'login', 'score')
    search_fields = ('gid', 'date_added', 'login', 'score')
    list_filter = ('date_added',)


admin.site.register(GitHubUser, GitHubUserAdmin)
