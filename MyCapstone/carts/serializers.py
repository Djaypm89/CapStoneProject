from rest_framework import serializers 
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'sizeRank', 'country', 'state', 'city', 
        'rent1YearAvg', 'rent5YearAvg', 'value1YearAvg','value5YearAvg']
        
   