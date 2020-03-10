from ..models import Stock
from rest_framework import serializers
from .indexSerializer import IndexSerializer 

class StockSerializer(serializers.ModelSerializer):
    index = IndexSerializer()

    class Meta:
        model = Stock
        fields = '__all__'
        read_only_field = ['id']
