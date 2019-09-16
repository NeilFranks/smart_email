from rest_framework import serializers
from .models import CategoryAlgorithmPair, EmailLogin, User


# CategoryAlgorithmPair Serializer
class CatAlgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAlgorithmPair
        fields = ('__all__')


# EmailLogin Serializer
class EmailLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLogin
        fields = ('__all__')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
