from .gmail import (
    connect_new_account,
    get_single_email,
    get_email_details,
    get_connected_addresses,
    get_emails_from_label,
    get_email_details_from_label,
    single_mark_as_read,
    single_mark_as_unread,
    batch_mark_as_read,
    batch_mark_as_unread,
    trash_message,
    batch_mark_as_something,
    batch_unmark_from_something,
    create_label,
)
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import (
    CategorySerializer,
    ConnectNewEmailSerializer,
    ConnectNewAccountSerializer,
    SingleEmailSerializer,
    EmailDetailsSerializer,
    ConnectedAddressesSerializer,
    EmailsFromLabelSerializer,
    McwFromLabelSerializer,
)
from .learn import mcw_from_label


class CategoryViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.request.user.category.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ConnectedEmailViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = ConnectNewEmailSerializer

    def get_queryset(self):
        return self.request.user.connectedEmail.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ConnectNewAccountViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = ConnectNewAccountSerializer

    def list(self, request):
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        content = {"content": connect_new_account(token)}
        results = ConnectNewAccountSerializer(content).data
        return Response(results.get("content"))


class SingleEmailViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = SingleEmailSerializer

    def list(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        data = request.data
        address = data.get("address")
        email_id = data.get("email_id")

        body = {"body": get_single_email(address, email_id, token)}
        results = SingleEmailSerializer(body).data
        return Response(results)


class EmailDetailsViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = EmailDetailsSerializer

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        try:
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        n = data.get("n")
        before_time = data.get("before_time")
        detailsList = {"detailsList": get_email_details(n, before_time, token)}

        results = EmailDetailsSerializer(detailsList).data
        return Response(results)


class EmailFromLabelViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = EmailDetailsSerializer

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        label = data.get("label")
        try:
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        detailsList = {"detailsList": get_email_details_from_label(label, token)}
        results = EmailDetailsSerializer(detailsList).data
        return Response(results)


class McwFromLabelViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = McwFromLabelSerializer

    def list(self, request):
        data = request.data
        label = data.get("label")
        try:
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        mcw = {"mcw": mcw_from_label(label, token)}
        results = McwFromLabelSerializer(mcw).data
        return Response(results)


class ConnectedAddressesViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = ConnectedAddressesSerializer

    def list(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        addresses = {"addresses": get_connected_addresses(token)}
        results = ConnectedAddressesSerializer(addresses).data
        return Response(results)


class SingleMarkAsReadViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        address = data.get("address")
        messageId = data.get("message_id")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        single_mark_as_read(address, messageId, token)


class SingleMarkAsUnreadViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        address = data.get("address")
        messageId = data.get("message_id")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        single_mark_as_unread(address, messageId, token)


class BatchMarkAsReadViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        address = data.get("address")
        messageId = data.get("message_id")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        batch_mark_as_read(address, messageId, token)


class BatchMarkAsUnreadViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        address = data.get("address")
        messageId = data.get("message_id")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        batch_mark_as_unread(address, messageId, token)


class TrashViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        address = data.get("address")
        messageId = data.get("message_id")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        trash_message(address, messageId, token)


class BatchMarkAsSomethingViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        address = data.get("address")
        messageIds = data.get("list_of_ids")
        labelList = data.get("list_of_labels")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        batch_mark_as_something(address, messageIds, labelList, token)


class BatchUnmarkFromSomethingViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        address = data.get("address")
        messageIds = data.get("list_of_ids")
        labelList = data.get("list_of_labels")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        batch_unmark_from_something(address, messageIds, labelList, token)


class CreateLabelViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    print("In ViewSet")

    def list(self, request):
        pass

    def post(self, request):
        print("In Post")
        data = request.data
        address = data.get("address")
        label = data.get("label_object")
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        create_label(address, label, token)
