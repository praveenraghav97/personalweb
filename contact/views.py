from django.shortcuts import render

# Create your views here.


def contact(request):

    if request.method == 'POST':
        print(request.POST['name'])
    return render(request, 'contact/contact-us.html')
