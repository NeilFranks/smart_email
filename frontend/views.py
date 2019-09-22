from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# @login_required(redirect_field_name="next", login_url=None)
def home(request):
    return render(request, "frontend/home.html")


def verify(request):
    return render(request, "googlea247c86106d85d33.html")
