from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'accounts/views/login.html')


def logout(request):
    return render(request, 'accounts/views/logout.html')


def register(request):
    return render(request, 'accounts/views/register.html')


def dashboard(request):
    return render(request, 'accounts/views/dashboard.html')