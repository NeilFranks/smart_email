from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
from sklearn.svm import LinearSVC


class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name="category", on_delete=models.CASCADE, null=True)

    

