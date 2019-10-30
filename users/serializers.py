from rest_framework import serializers
from .models import EmailToken


class EmailTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailToken
        fields = ('__all__')
