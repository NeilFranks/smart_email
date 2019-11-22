from rest_framework import serializers
from .models import Category, ConnectedEmail


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ConnectNewEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectedEmail
        fields = "__all__"


class ConnectNewAccountSerializer(serializers.Serializer):
    content = serializers.DictField()


class SingleEmailSerializer(serializers.Serializer):
    body = serializers.CharField()


class EmailDetailsSerializer(serializers.Serializer):
    detailsList = serializers.ListField()


class ConnectedAddressesSerializer(serializers.Serializer):
    addresses = serializers.ListField()


class McwFromLabelSerializer(serializers.Serializer):
    mcw = serializers.ListField()


class EmailsFromLabelSerializer(serializers.Serializer):
    detailsList = serializers.ListField()
