from django.db import models

#DDL + DML
class Curriculum(models.Model):
    name = models.CharField(max_length=255)
