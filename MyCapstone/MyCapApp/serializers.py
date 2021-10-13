# from django import serializers
from rest_framework import serializers 
from .models import HousingData
# from .models import DataCart



class HousingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingData
        fields = ['id', 'sizeRank', 'country', 'state', 'city', 
        'rent1YearAvg', 'rent5YearAvg', 'value1YearAvg','value5YearAvg']
        
        # add 'user_id' ??


# class DataCartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DataCart
#         fields = ['id', 'sizeRank', 'country', 'state', 'city', 
#         'rent1YearAvg', 'rent5YearAvg', 'value1YearAvg','value5YearAvg',
#         'user_Id']
        
        #  'user_id' added because DataCart will require user reg and login. 
