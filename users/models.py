from django.db import models
from django.contrib.auth.models import User


class CategoryAlgorithmPair(models.Model):
    category = models.CharField(max_length=50)
    algorithm = models.CharField(max_length=100)
    time = models.DateTimeField()
    owner = models.ForeignKey(
        User, related_name="catAlgPairs", on_delete=models.CASCADE, null=True)


class TestObject(models.Model):
    testObject = models.TextField(null=True)
