from rest_framework import viewsets, permissions
from .serializers import CatAlgSerializer

# CategoryAlgorithmPair Viewset


class CatAlgViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,  # need to restrict this permission
    ]

    serializer_class = CatAlgSerializer

    def get_queryset(self):
        return self.request.user.catAlgPairs.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
