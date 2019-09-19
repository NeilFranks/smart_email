from rest_framework import serializers
from .models import CategoryAlgorithmPair

# CategoryAlgorithmPair Serializer


class CatAlgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAlgorithmPair
        fields = ('__all__')
