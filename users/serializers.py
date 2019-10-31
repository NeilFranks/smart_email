from rest_framework import serializers
from .models import ConnectedEmail


class ConnectedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectedEmail
        fields = ('__all__')
