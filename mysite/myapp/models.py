from audioop import mul
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Details(models.Model):

    fullname = models.CharField(max_length=50, default='',null=False)
    email = models.EmailField(max_length=60)
    supplier = models.CharField( max_length=200)
    phone_number = models.IntegerField()
    unit = models.IntegerField()
    location = models.TextField(max_length=100)

    def __str__(self):
       return self.fullname

class cDetails(models.Model):

    cname = models.CharField(max_length=50, default='',null=False)
    cemail = models.EmailField(max_length=60)
    cphone_number = models.IntegerField()
    clocation = models.TextField(max_length=100)

    def __str__(self):
       return self.cname
    
