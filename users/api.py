from .models import CategoryAlgorithmPair, EmailLogin, User
from rest_framework import viewsets, permissions
from .serializers import CatAlgSerializer, EmailLoginSerializer, UserSerializer

# CategoryAlgorithmPair Viewset


class CatAlgViewSet(viewsets.ModelViewSet):
    queryset = CategoryAlgorithmPair.objects.all()  # get all catAlgs
    permissions_classes = [
        permissions.AllowAny  # need to restrict this permission
    ]
    serializer_class = CatAlgSerializer

# EmailLogin Viewset


class EmailLoginViewSet(viewsets.ModelViewSet):
    queryset = EmailLogin.objects.all()  # get all Emaillogins
    permissions_classes = [
        permissions.AllowAny  # need to restrict this permission
    ]
    serializer_class = EmailLoginSerializer

# User Viewset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # get all Users
    permissions_classes = [
        permissions.AllowAny  # need to restrict this permission
    ]
    serializer_class = UserSerializer
