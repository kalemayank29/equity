from django.db import models

# Create your models here.
class Stock(models.Model):
    tickr = models.CharField(max_length=200, primary_key=True)
    price = models.IntegerField()
    eps = models.IntegerField(default=0)
    pe = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)

    def __str__(self):
        return self.tickr


class Pick(models.Model):
    uid = models.IntegerField(unique=True)
    tickr = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.IntegerField()

    def __str__(self):
        return self.tickr
