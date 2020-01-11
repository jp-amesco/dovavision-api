from ..models import Company
from rest_framework import serializers
from ..DynamicFieldsModelSerializer import DynamicFieldsModelSerializer 

class CompanySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'country', 'is_active']
        read_only_field = ['id']
