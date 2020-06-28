from ..models import Stock
from rest_framework import serializers
from .indexSerializer import IndexSerializer 
from dovavision.serializers.companySerializer import CompanySerializer

class StockSerializer(serializers.ModelSerializer):
    index = IndexSerializer()
    company = CompanySerializer()

    class Meta:
        model = Stock
        fields = '__all__'
        read_only_field = ['id']
