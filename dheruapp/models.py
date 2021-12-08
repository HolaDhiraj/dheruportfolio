from django.db import models

# Create your models here.
class ClientModel(models.Model):
    Userid = models.CharField(max_length=10)
    Phone = models.CharField(max_length=10)