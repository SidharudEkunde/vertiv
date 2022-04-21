from rest_framework import serializers
from system.models import System


class SystemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = System
        fields = ["id", "sysid", "name", "image"]


class SystemHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ['id', 'sysid', 'name']
