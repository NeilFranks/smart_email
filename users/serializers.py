from rest_framework import serializers
from .models import CategoryAlgorithmPair, TestObject

# CategoryAlgorithmPair Serializer


class CatAlgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAlgorithmPair
        fields = ('__all__')


class TestObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestObject
        fields = ('__all__')
