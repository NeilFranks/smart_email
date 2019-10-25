from django.db import models
from django.contrib.auth.models import User


class EmailPass(models.Model):
    email = models.CharField(max_length=100)
    appPass = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, related_name="emailPass", on_delete=models.CASCADE, null=True)
