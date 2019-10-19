from rest_framework import viewsets, permissions
from .models import TestObject
from .serializers import CatAlgSerializer, TestObjectSerializer

# CategoryAlgorithmPair Viewset


class CatAlgViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = CatAlgSerializer

    def get_queryset(self):
        return self.request.user.catAlgPairs.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TestObjectViewSet(viewsets.ModelViewSet):
    queryset = TestObject.objects.all()  # get all catAlgs
    permissions_classes = [
        permissions.AllowAny  # need to restrict this permission
    ]
    serializer_class = TestObjectSerializer
