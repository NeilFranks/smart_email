from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# @login_required(redirect_field_name="next", login_url=None)
def home(request):
    return render(request, "frontend/home.html")


def base(request):
    return render(request, "frontend/registration/base.html")


def emailConnect(request):
    return render(request, "frontend/emailConnect.html")


def emailView(request):
    return render(request, "frontend/emailView.html")


def makeCategory(request):
    return render(request, "frontend/MakeCategory.html")
