from django.db import models
# Create your models here.
from sensors.models import TemperatureHumidity


class Alert(models.Model):
    """ Model for Alert"""

    macid = models.ForeignKey(TemperatureHumidity, on_delete=models.CASCADE)
    value = models.IntegerField()
    lastseen = models.DateTimeField()
