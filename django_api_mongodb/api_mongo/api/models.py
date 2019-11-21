#from django.db import models

from djongo import models
# Create your models here.


class User(models.Model):
    password = models.CharField(max_length = 8)
    comp_id  = models.IntegerField()
    tel = models.IntegerField()
    username = models.CharField(max_length = 30)

class Company(models.Model):
    comp_id = models.IntegerField()
    comp_name  = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    tel = models.IntegerField()
