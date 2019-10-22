from django.contrib import admin
from django.apps import AppConfig
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']


admin.register(Comment, CommentAdmin)


