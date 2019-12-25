from rest_framework import serializers
from .models import User
from .DynamicFieldsModelSerializer import DynamicFieldsModelSerializer 

class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_field = ['id']
