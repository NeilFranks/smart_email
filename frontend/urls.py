from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('privacy-policy', views.policy),
]
