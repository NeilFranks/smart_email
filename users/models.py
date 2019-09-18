from django.db import models
from django.contrib.auth.models import User


class CategoryAlgorithmPair(models.Model):
    category = models.CharField(max_length=50)
    algorithm = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, related_name="catAlgPairs", on_delete=models.CASCADE, null=True)


class EmailLogin(models.Model):
    emailAddress = models.EmailField(max_length=100, unique=True)
    emailPass = models.CharField(max_length=100)


class myUser(models.Model):
    name = models.CharField(max_length=100)
    categoryAlgorithmPairs = models.ManyToManyField('CategoryAlgorithmPair')
    emailLogins = models.ManyToManyField('EmailLogin')
