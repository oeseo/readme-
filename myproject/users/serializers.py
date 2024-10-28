from rest_framework import serializers
from .models import CustomUser, Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'full_name', 'position', 'is_dismissed', 'dismissed_date']    
