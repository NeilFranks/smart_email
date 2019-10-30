from rest_framework import viewsets, permissions
from .serializers import EmailTokenSerializer


class EmailTokenViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = EmailTokenSerializer

    def get_queryset(self):
        return self.request.user.emailToken.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
