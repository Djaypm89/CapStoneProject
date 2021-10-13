from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HousingData(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    sizeRank = models.IntegerField()
    country = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    rent1YearAvg = models.IntegerField()
    rent5YearAvg = models.IntegerField()
    value1YearAvg = models.IntegerField()
    value5YearAvg = models.IntegerField()
    
    # // change below so form can accept floats or remove and have ratio not stored in DB, but displayed thru a function? //
    # ratio = models.FloatField(max_length=50) 
    
# class DataCart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     sizeRank = models.IntegerField()
#     country = models.TextField(max_length=50)
#     state = models.TextField(max_length=50)
#     city = models.TextField(max_length=50)
#     rent1YearAvg = models.IntegerField()
#     rent5YearAvg = models.IntegerField()
#     value1YearAvg = models.IntegerField()
#     value5YearAvg = models.IntegerField()
