from django.db import models


# Create your models here.

class Input(models.Model):
    func = models.CharField(max_length=100)
    inicial = models.FloatField()
