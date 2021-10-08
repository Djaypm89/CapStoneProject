from django.db import models

# Create your models here.
class HousingData(models.Model):
    sizeRank = models.IntegerField(max_length=50)
    country = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    rent1YearAvg = models.IntegerField(max_length=50)
    rent5YearAvg = models.IntegerField(max_length=50)
    value1YearAvg = models.IntegerField(max_length=50)
    value5YearAvg = models.IntegerField(max_length=50)
    
    # // change below so form can accept floats or remove and have ratio not stored in DB, but displayed thru a function? //
    # ratio = models.FloatField(max_length=50) 
    


