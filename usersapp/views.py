from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Oops..Wrong Password!!")
                return redirect('users:login')
        else:
            messages.error(request, "Email not found..Use another or Register..")
            return redirect('users:login')

    else:
        return render(request, 'users/login.html')


def signup(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Dear ' + first_name + '!, I think you are registered already..Can you please'
                                                           ' try Login!!')
            return redirect('users:signup')
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                        password=password1)
        user.save()
        messages.success(request, 'Welcome ' + first_name + '..Go ahead to Login!!')
        return redirect('users:login')
    else:
        return render(request, 'users/register.html', context)


@login_required(login_url='/users/login/')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect('users:login')

