from django.shortcuts import render


def home(request):
    return render(request, 'frontend/home.html')


def base(request):
    return render(request, 'frontend/registration/base.html')
