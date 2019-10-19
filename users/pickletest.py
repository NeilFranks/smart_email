import requests
import base64
from django.core import serializers


class TestObject(object):
    def __init__(self, name, age, listThing):
        self.name = name
        self.age = age
        self.listThing = listThing


SaveThisThing = TestObject("horbus", 25, [13, 542, 53, 12, 86])

data = serializers.serialize("json", SaveThisThing)

requests.post('http://127.0.0.1:8000/api/testObject',
              json=data)


r = requests.get('http://127.0.0.1:8000/api/testObject/7/')

b = base64.encodestring(SaveThisThing)
