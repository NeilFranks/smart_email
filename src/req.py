import requests
import base64
from django.core import serializers


# class TestObject(object):
#     def __init__(self, name, age, listThing):
#         self.name = name
#         self.age = age
#         self.listThing = listThing


# SaveThisThing = TestObject("horbus", 25, [13, 542, 53, 12, 86])

# data = serializers.serialize("json", SaveThisThing)

# requests.post('http://127.0.0.1:8000/api/testObject',
#               json=data)


r = requests.get('http://127.0.0.1:8000/api/et/',
                 headers={'Authorization': 'Token 11997d9aed82385d4811947006edd0ea3af2e9a75881ed5d57da13285b9aa42c'})

a = 10
