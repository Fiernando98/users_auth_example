from rest_framework import serializers

from .models import CustomProfile


class CustomProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomProfile
        fields = '__all__'
