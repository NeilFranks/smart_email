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
from .learn import (
    mcw_from_label,
    classifier_from_emails_and_notEmails,
    update_classifier_from_emails_and_notEmails,
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
from rest_framework.authtoken.models import Token

from .learn import classifier_from_label, extract_features
from .models import Category

import codecs
import json
import os
import pickle
import requests
import time
import base64


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
        encoded_label_id = data.get("label_id")
        if encoded_label_id:
            label_id = pickle.loads(codecs.decode(encoded_label_id.encode(), "base64"))
        else:
            label_id = None

        detailsList = {
            "detailsList": get_email_details(n, before_time, label_id, token)
        }

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
        n = data.get("n")
        if not n:
            n = 30
        try:
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        detailsList = {"detailsList": get_email_details_from_label(n, label, token)}
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

        # batch_mark_as_something(address, messageIds, labelList, token)


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

        # batch_unmark_from_something(address, messageIds, labelList, token)


class SetPageLabelsViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):

        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        # Emails need to have body/subject/id/address
        emails = data.get("emails")

        # get categories
        response = requests.get(
            "%s/api/category/" % baseURL(), headers={"Authorization": token}
        )

        # turn categories into a dictionary
        categories = json.loads(response.content)

        # will be all emails that were deemed to fit some category (use to find how many were moved)
        fitList = []
        totalMoved = 0

        # For each category saved
        for category in categories:
            addressDict = dict()

            # grab the label_ids, classifier, and most common words from each category
            email_label_ids = pickle.loads(base64.b64decode(category["label_id"]))
            svc = pickle.loads(base64.b64decode(category["classifier"]))
            mcw = pickle.loads(base64.b64decode(category["mcw"]))

            # generate feature matrix from the given emails
            # print(emails)
            # print(mcw)
            matrix = extract_features(mcw, emails)

            # predict with saved model
            email_predictions = svc.predict(matrix)

            # For each prediction
            for i in range(len(email_predictions)):

                # if the model predicted that the email should be in the label
                if email_predictions[i] == 1:
                    category_label = email_label_ids[emails[i].get("address")][0]
                    already_labels = emails[i].get("labels")

                    if category_label not in already_labels:
                        print(category_label)
                        print(already_labels)
                        totalMoved += 1

                    # populate addressDict with only emails that are predicted
                    address = emails[i].get("address")
                    if address in addressDict:
                        addressDict[address].append(emails[i].get("id"))
                    else:
                        addressDict[address] = [emails[i].get("id")]

            # Mark all emails in addressDict with that proper label
            batch_mark_as_something(addressDict, email_label_ids, token)

        print(totalMoved)
        return Response(data=totalMoved)


class CreateLabelViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        data = request.data
        label = data.get("label")
        emails = data.get("emails")
        notEmails = data.get(
            "notEmails"
        )  # these are emails that should NOT be in the category.
        try:
            data = request.data
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        # create the label in GMail world
        label_object = {
            "labelListVisibility": "labelShow",
            "messageListVisibility": "show",
            "name": label,
        }
        create_label_response = create_label(label_object, token)
        # check if there was an error with creating the label
        if (
            hasattr(create_label_response, "status")
            and create_label_response.status != 200
        ):
            # return the error without any additional action
            return Response(
                data=create_label_response, status=create_label_response.status
            )

        # move emails into label
        addressDict = dict()
        for email in emails:
            address = email.get("address")
            if address in addressDict:
                addressDict[address].append(email.get("id"))
            else:
                addressDict[address] = [email.get("id")]

        # create_label_response should be a dictionary; keys are email addresses, values are associated label_id for the label
        batch_mark_as_something(addressDict, create_label_response, token)

        # train a model
        classifier, mcw = classifier_from_label(create_label_response, notEmails, token)

        print(mcw)

        # save to database
        pickledSVC = codecs.encode(pickle.dumps(classifier), "base64").decode()
        pickledLabelDict = codecs.encode(
            pickle.dumps(create_label_response), "base64"
        ).decode()
        pickledMCW = codecs.encode(pickle.dumps(mcw), "base64").decode()

        response = requests.post(
            "%s/api/category/" % baseURL(),
            headers={"Authorization": token},
            json={
                "name": label,
                "mcw": pickledMCW,
                "label_id": pickledLabelDict,
                "classifier": pickledSVC,
            },
        )

        return Response(data=response, status=response.status_code)


class RetrainLabelViewSet(viewsets.GenericViewSet):
    permissions_classes = [permissions.IsAuthenticated]

    def list(self, request):
        pass

    def post(self, request):
        print("start")
        data = request.data

        try:
            # auth is in headers like this when request comes from front end
            headers = data.get("headers")
            token = headers.get("Authorization")
        except AttributeError:
            # auth is like this when request comes from postman
            token = request.META.get("HTTP_AUTHORIZATION")

        label = data.get("label")
        n = data.get("n")  # there will be n emails that SHOULD be in category
        notEmails = data.get(
            "notEmails"
        )  # these are emails that should NOT be in the category.

        # STEP ONE: move notEmails out of the category
        # decode label_id
        label_id = pickle.loads(base64.b64decode(label["label_id"]))

        addressDict = dict()
        notEmailIds = []
        for email in notEmails:
            notEmailIds.append(email["id"])
            address = email.get("address")
            if address in addressDict:
                addressDict[address].append(email.get("id"))
            else:
                addressDict[address] = [email.get("id")]

        batch_unmark_from_something(addressDict, label_id, token)

        print("Moved False-Positive emails out of category")

        # STEP TWO: get n email from category

        # just want most recent emails
        try:
            emails = get_email_details_from_label(n, label_id, token)

            print("got %s most recent emails from %s" % (n, label["name"]))

            # STEP 3: train a new model
            classifier = pickle.loads(base64.b64decode(label["classifier"]))

            classifier, mcw = update_classifier_from_emails_and_notEmails(
                classifier, label, emails, notEmails, token
            )

            print("model has been trained")

            # save to database
            pickledSVC = codecs.encode(pickle.dumps(classifier), "base64").decode()
            pickledMCW = codecs.encode(pickle.dumps(mcw), "base64").decode()

            response = requests.put(
                "%s/api/category/%s/" % (baseURL(), label["id"]),
                headers={"Authorization": token},
                json={
                    "id": label["id"],
                    "name": label["name"],
                    "label_id": label["label_id"],
                    "mcw": pickledMCW,
                    "classifier": pickledSVC,
                },
            )

            return Response(data=response, status=response.status_code)

        except:
            # something bad happened, put False-Positive emails back in!
            batch_mark_as_something(addressDict, label_id, token)

            return Response(status=500)


def baseURL():
    # in Procfile for heroku, BASE_URL should be set to `export BASE_URL=https://capstone-smart-email.herokuapp.com/`
    try:
        baseURL = os.environ["BASE_URL"]
    except KeyError:
        baseURL = "http://127.0.0.1:8000"

    # print("baseURL set to %s" % baseURL)
    return baseURL
