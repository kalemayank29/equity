from django.db import models

# Create your models here.
class Stock(models.Model):
    tickr = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.tickr
