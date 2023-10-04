from django.db import models

# Create your models here.


class CarModel(models.Model):
    class Meta():
        db_table = 'car'
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    countPlace = models.IntegerField()
    typeCar = models.CharField(max_length=50)
    capacityEngine = models.FloatField()
    
    