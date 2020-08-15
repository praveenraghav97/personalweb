from django.urls import path

from myprofile import views

urlpatterns = [
    path('', views.my_profile, name='my-profile')
]