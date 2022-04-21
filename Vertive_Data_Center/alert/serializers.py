from rest_framework import serializers
from sensors.serialzers import TemperatureHumiditySerializer
from .models import Alert

""" Serializer for Alert model"""


class AlertSerializer(serializers.ModelSerializer):
    macid = TemperatureHumiditySerializer()

    class Meta:
        model = Alert
        fields = '__all__'
