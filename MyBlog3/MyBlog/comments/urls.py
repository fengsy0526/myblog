from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),

]
