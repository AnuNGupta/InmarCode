from django.db import models

# Create your models here.


class Location(models.Model):
    locationname = models.CharField(max_length=100)
    departmentname = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    