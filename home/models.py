from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
    username=models.TextField(max_length=50, primary_key=True)
    password=models.TextField()
    name=models.TextField()
    date_of_birth=models.DateField()
    avatar=models.TextField()
    email=models.TextField(max_length=100)
    phone=models.TextField(max_length=20)
    address=models.TextField()

class News(models.Model):
    # id=models.AutoField(primary_key=True)
    title=models.TextField()
    content=models.TextField()
    author=models.TextField(max_length=100)