from .gmail import connect_new_account, get_single_email, get_email_details, get_connected_addresses
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import ConnectNewEmailSerializer, ConnectNewAccountSerializer, SingleEmailSerializer, EmailDetailsSerializer, ConnectedAddressesSerializer


class ConnectedEmailViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = ConnectNewEmailSerializer

    def get_queryset(self):
        return self.request.user.connectedEmail.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ConnectNewAccountViewSet(viewsets.GenericViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = ConnectNewAccountSerializer

    def list(self, request):
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get('HTTP_AUTHORIZATION')
        content = {"content": connect_new_account(token)}
        results = ConnectNewAccountSerializer(content).data
        return Response(results.get("content"))


class SingleEmailViewSet(viewsets.GenericViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = SingleEmailSerializer

    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        data = request.data
        address = data.get("address")
        email_id = data.get("email_id")

        body = {"body": get_single_email(address, email_id, token)}
        results = SingleEmailSerializer(body).data
        return Response(results)


class EmailDetailsViewSet(viewsets.GenericViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = EmailDetailsSerializer

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        n = data.get("n")
        try:
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get('HTTP_AUTHORIZATION')

        detailsList = {"detailsList": get_email_details(n, token)}
        results = EmailDetailsSerializer(detailsList).data
        return Response(results)


class ConnectedAddressesViewSet(viewsets.GenericViewSet):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = ConnectedAddressesSerializer

    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        addresses = {"addresses": get_connected_addresses(token)}
        results = ConnectedAddressesSerializer(addresses).data
        return Response(results)
