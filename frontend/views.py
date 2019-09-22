from django.shortcuts import render


# @login_required(redirect_field_name="next", login_url=None)
def home(request):
    return render(request, "frontend/home.html")
