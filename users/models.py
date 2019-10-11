from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
from sklearn.svm import LinearSVC

class CommonWords(models.Model):
    word = models.CharField(max_length=128)
    count = models.IntegerField()

class SeparatedValuesField(models.TextField):

    def __init__(self, *args, **kwargs):
        print(kwargs)
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def get_db_prep_value(self, value, connection, prepared):
        if not value: return
        value = value.split()
        assert(isinstance(value, list) or isinstance(value, tuple))
        print([str(s) for s in value])
        return self.token.join([str(s) for s in value])

    # def value_to_string(self, obj):
    #     value = self._get_val_from_obj(obj)
    #     return self.get_db_prep_value(value)

class Emails(models.Model):
    sender = models.EmailField(max_length=128)
    subject = models.CharField(max_length=2048)
    body = models.TextField()

class CategoryAlgorithmPair(models.Model):
    category = models.CharField(max_length=50)
    common_words = SeparatedValuesField(default=["dog", "cat"])
    # model = PickledObjectField(default=" ") # the 
    emails = SeparatedValuesField(default=["dog", "cat"])
    owner = models.ForeignKey(
        User, related_name="catAlgPairs", on_delete=models.CASCADE, null=True)
    

