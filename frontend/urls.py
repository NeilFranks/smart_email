from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("base", views.base),
    path("emailConnect", views.emailConnect),
    path("makeCategory", views.makeCategory),
    path("retrainCategory", views.retrainCategory),
]
