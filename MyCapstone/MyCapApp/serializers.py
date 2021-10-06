# from django import serializers
from rest_framework import serializers 
from .models import HousingData


class HousingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingData
        fields = ['id', 'country', 'state', 'city', 'rent', 'price', 'ratio']
        