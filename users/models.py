from django.db import models
from django.contrib.auth.models import User


class ConnectedEmail(models.Model):
    creds = models.TextField()
    address = models.TextField()
    owner = models.ForeignKey(
        User, related_name="connectedEmail", on_delete=models.CASCADE, null=True)
