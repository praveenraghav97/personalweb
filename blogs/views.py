from django.shortcuts import render
from .models import Blog

# Create your views here.


def blog_home(request):
    context = {}

    blogs = Blog.objects.all()
    context['blogs'] = blogs
    return render(request, 'blogs/blog-home.html', context)
