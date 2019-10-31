from rest_framework import viewsets, permissions
from .serializers import ConnectedEmailSerializer


class ConnectedEmailViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = ConnectedEmailSerializer

    def get_queryset(self):
        return self.request.user.connectedEmail.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
