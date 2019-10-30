from django.db import models
from django.contrib.auth.models import User


class EmailToken(models.Model):
    emailToken = models.TextField()
    owner = models.ForeignKey(
        User, related_name="emailToken", on_delete=models.CASCADE, null=True)
