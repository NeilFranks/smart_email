from django.db import models


class CategoryAlgorithmPair(models.Model):
    category = models.CharField(max_length=50)
    algorithm = models.CharField(max_length=100)


class EmailLogin(models.Model):
    emailAddress = models.EmailField(max_length=100, unique=True)
    emailPass = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    categoryAlgorithmPairs = models.ManyToManyField('CategoryAlgorithmPair')
    emailLogins = models.ManyToManyField('EmailLogin')
