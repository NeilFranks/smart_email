from rest_framework import serializers
from .models import ConnectedEmail


class ConnectNewEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectedEmail
        fields = ('__all__')


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
