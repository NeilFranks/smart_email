from rest_framework import viewsets, permissions
from .serializers import EmailPassSerializer


class EmailPassViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,  # need to restrict this permission
    ]

    serializer_class = EmailPassSerializer

    def get_queryset(self):
        return self.request.user.emailPass.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
