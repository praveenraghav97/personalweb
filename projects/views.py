from django.shortcuts import render
from .models import Project

# Create your views here.


def projects_home(request):
    context = {}
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'projects/projects-home.html', context)


def create_project(request):
    context = {}
    if request.method == 'POST':
        return render(request, 'projects/added.html')

    else:
        return render(request, 'projects/create-project.html')

