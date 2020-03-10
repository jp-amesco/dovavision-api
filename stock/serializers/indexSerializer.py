from ..models import Index
from rest_framework import serializers

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = '__all__'
        read_only_field = ['id']
