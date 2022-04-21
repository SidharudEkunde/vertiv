from django.db import models
# Create your models here.
from system.models import System


class TemperatureHumidity(models.Model):
    """ Model for temperature-humidity """
    macid = models.CharField(max_length=50, unique=True, db_index=True, null=False)
    temperature = models.FloatField()
    # humidity = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
    lastseen = models.DateTimeField(auto_now=True)
    systemid = models.ForeignKey(System, on_delete=models.CASCADE)
    battery = models.FloatField()


class DailyTemperatureHumidity(models.Model):
    """ DailyTemperatureHumidity model"""

    temperature = models.FloatField()
    # humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    asset = models.ForeignKey(TemperatureHumidity, on_delete=models.CASCADE)


class WeeklyTemperatureHumidity(models.Model):
    """ weeklyTemperatureHumidity model"""
    temperature = models.FloatField()
    # humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    asset = models.ForeignKey(TemperatureHumidity, on_delete=models.CASCADE)


class MonthlyTemperatureHumidity(models.Model):
    """ MonthlyTemperatureHumidity model"""

    temperature = models.FloatField()
    # humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    asset = models.ForeignKey(TemperatureHumidity, on_delete=models.CASCADE)


class IAQ(models.Model):
    """Model for IAQ sensor"""
    macid = models.CharField(max_length=40, unique=True)
    co2 = models.FloatField()
    tvoc = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    room = models.CharField(max_length=100)
    lastseen = models.DateTimeField(auto_now=True)
    battery = models.FloatField()
    # floor = models.ForeignKey(FloorMap, on_delete=models.CASCADE)
