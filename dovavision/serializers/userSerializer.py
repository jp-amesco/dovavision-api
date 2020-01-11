from ..models import User
from rest_framework import serializers
from .companySerializer import CompanySerializer
from ..DynamicFieldsModelSerializer import DynamicFieldsModelSerializer 

class UserSerializer(DynamicFieldsModelSerializer):
    company_set = CompanySerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_field = ['id']
