from django.test import TestCase
from django.test import Client
# Create your tests here.

c = Client()
c.get('/login/')