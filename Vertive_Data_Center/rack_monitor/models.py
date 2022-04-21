from django.db import models
from sqlalchemy.sql.functions import mode
# Create your models here.

#
# class Rack(models.Model):
#     macid = models.CharField(max_length=40, unique=True)
#     floor = models.ForeignKey(FloorMap, on_delete=models.CASCADE)
#     pdu = models.CharField(max_length=40)
#     capacity = models.FloatField()
#     x = models.FloatField()
#     y = models.FloatField()
#     x1 = models.FloatField()
#     y1 = models.FloatField()


# class RackTracking(models.Model):
#     rackid = models.ForeignKey(Rack, on_delete=models.CASCADE)
#     tagid = models.ForeignKey(Asset, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(null=True)

