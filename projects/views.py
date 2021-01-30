from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from .models import Project

# Create your views here.


def projects_home(request):
    context = {}
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'projects/projects-home.html', context)


@login_required (login_url='users/login/')
def create_project(request):
    context = {}
    if request.method == 'POST':
        if auth.user.email == 'praveenraghav04@gmail.com':
            title = request.POST['title']
            description = request.POST['description']

            project = Project.objects.create(title=title, description=description)
            project.save()
            context = {"message": "Project added Successfully"}
            return render(request, 'projects/added.html', context)
        else:
            context = {"message": "You are not allowed to add Project"}
            return render(request, 'projects/create-project.html', context)




    else:
        return render(request, 'projects/create-project.html')

