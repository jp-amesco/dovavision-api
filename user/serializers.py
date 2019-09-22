from rest_framework import serializers
from . import models 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            date_of_birth=validated_data['date_of_birth'],
            password=validated_data['password']
        )
        return user

        
