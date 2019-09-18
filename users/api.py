from .models import CategoryAlgorithmPair, EmailLogin, myUser
from rest_framework import viewsets, permissions
from .serializers import CatAlgSerializer, EmailLoginSerializer, UserSerializer

# CategoryAlgorithmPair Viewset


class CatAlgViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated  # need to restrict this permission
    ]

    serializer_class = CatAlgSerializer

    def get_queryset(self):
        return self.request.user.catAlgs.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# EmailLogin Viewset
class EmailLoginViewSet(viewsets.ModelViewSet):
    queryset = EmailLogin.objects.all()  # get all Emaillogins
    permissions_classes = [
        permissions.AllowAny  # need to restrict this permission
    ]
    serializer_class = EmailLoginSerializer

# User Viewset


class UserViewSet(viewsets.ModelViewSet):
    queryset = myUser.objects.all()  # get all Users
    permissions_classes = [
        permissions.AllowAny  # need to restrict this permission
    ]
    serializer_class = UserSerializer
