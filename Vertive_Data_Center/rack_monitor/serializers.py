from rest_framework import serializers
from .models import Rack


"""Serializer for Rack model"""
class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = '__all__'
