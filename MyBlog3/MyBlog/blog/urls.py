from django.contrib import admin
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.details, name='details')
]
