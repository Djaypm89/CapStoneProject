# from django import serializers
from rest_framework import serializers 
from .models import HousingData


class HousingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingData
        fields = ['id', 'sizeRank' 'country', 'state', 'city', 
        'rent1YearAvg', 'rent5YearAvg', 'value1YearAvg','value5YearAvg',
        'price', 'ratio']
        