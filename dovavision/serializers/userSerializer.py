from ..models import User
from rest_framework import serializers
from stock.serializers.stockSerializer import StockSerializer
from ..DynamicFieldsModelSerializer import DynamicFieldsModelSerializer 

class UserSerializer(DynamicFieldsModelSerializer):
    stock_set = StockSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_field = ['id']
        extra_kwargs = {'password': {'write_only': True}}
