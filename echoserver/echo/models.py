from django.db import models


# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    year_of_birth = models.PositiveIntegerField(null=True)
