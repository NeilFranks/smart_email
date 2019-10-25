from rest_framework import serializers
from .models import EmailPass


class EmailPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailPass
        fields = ('__all__')
