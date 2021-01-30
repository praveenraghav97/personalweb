from django.urls import path

from projects import views


app_name = 'projects'
urlpatterns = [
    path('', views.projects_home, name='projects-home'),
    path('create_project', views.create_project, name='create-project' )
]

