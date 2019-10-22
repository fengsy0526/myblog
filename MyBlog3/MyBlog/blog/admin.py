from django.contrib import admin
from .models import Post, Category, Tag
from django.apps import AppConfig
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '博客'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

