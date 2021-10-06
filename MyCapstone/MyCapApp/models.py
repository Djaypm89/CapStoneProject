from django.db import models

# Create your models here.
class HousingData(models.Model):
    country = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    rent = models.IntegerField(max_length=50)
    price = models.IntegerField(max_length=50)
    # // change below so form can accept floats or remove and have ratio not stored in DB, but displayed thru a function? //
    ratio = models.FloatField(max_length=50) 
    


