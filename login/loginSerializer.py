from rest_framework import serializers
from user.models import User

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'email', 'password', 'birth')
