from django.db import models

class Farm(models.Model):
    name = models.CharField(max_length=200)

class Field(models.Model):
    CHOICES = ( ("CABBAGE", "Cabbage"), ("POTATOES", "Potatoes"), ("WHEAT", "Wheat"),)
    farm = models.ForeignKey(Farm, on_delete=models.DO_NOTHING)
    last_sewn = models.DateTimeField(null=True,blank=True)
    latitude = models.PointField()
    longitude = models.PointField()
    name = models.CharField(max_length=200)
    produce = models.CharField(choices=CHOICES, default="WHEAT")
    size = models.FloatField(null=True, blank=True, default=0.0)