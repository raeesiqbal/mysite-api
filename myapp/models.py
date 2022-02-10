from operator import mod
from platform import mac_ver
from pyexpat import model
from django.db import models

# Create your models here.
class Data(models.Model):
    domain = models.CharField(max_length=200)
    api = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.domain}"
