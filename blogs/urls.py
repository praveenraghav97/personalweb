from django.urls import path

from blogs import views


app_name = 'blogs'
urlpatterns = [
    path('', views.blog_home, name='blog-home')
]