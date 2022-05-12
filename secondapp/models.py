from calendar import month
from unicodedata import name
from django.db import models
from django.forms import CharField

class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()

class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()
    class Meta:
        db_table = 'army_shop'
        managed = False