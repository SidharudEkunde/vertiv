from django.db import models


class System(models.Model):
    name = models.CharField(max_length=40, unique=True)
    sysid = models.IntegerField()
    image = models.ImageField(upload_to='static/tracking/')
    capacity = models.IntegerField(default=3)




