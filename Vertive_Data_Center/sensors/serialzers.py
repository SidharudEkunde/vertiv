from rest_framework import serializers

from sensors.models import TemperatureHumidity, DailyTemperatureHumidity
from system.serializers import SystemSerializer, SystemHealthSerializer


class TemperatureHumiditySerializer(serializers.ModelSerializer):
    """Serializer for TempHumidity Model"""

    # systemid = SystemSerializer()

    class Meta:
        model = TemperatureHumidity
        fields = '__all__'
        # fields = ['rackid', 'macid', 'temperature' , 'humidity', 'position', 'x', 'y']


class SensorSerializer(serializers.ModelSerializer):
    # asset = TemperatureHumiditySerializer()

    class Meta:
        model = DailyTemperatureHumidity
        # fields = "__all__"
        fields = ['temperature', 'timestamp']


class TemperatureHealthSerializer(serializers.ModelSerializer):
    systemid = SystemHealthSerializer()

    class Meta:
        model = TemperatureHumidity
        fields = '__all__'
