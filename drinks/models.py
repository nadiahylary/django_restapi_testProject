from django.db import models


# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    has_alcohol = models.BooleanField()

    def __str__(self):
        return f"{self.name}"
