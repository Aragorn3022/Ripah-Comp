from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.models import Permission

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description=models.TextField(max_length=500)
    Category=models.TextField(max_length=500)
    itemPictureLocation=models.CharField(max_length=50)
