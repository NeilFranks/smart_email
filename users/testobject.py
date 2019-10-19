import base64

from django.db import models


class Foo(models.Model):
    _data = models.TextField(
        db_column='data',
        blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)
