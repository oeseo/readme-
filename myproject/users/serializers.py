from rest_framework import serializers
from .models import CustomUser, Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'full_name', 'position', 'is_dismissed', 'dismissal_date']
