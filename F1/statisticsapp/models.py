from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


from django.db import models


class DriverResult(models.Model):
    driverID = models.CharField(max_length=30)
    driver = models.CharField(max_length=30)
    position = models.IntegerField()
    points = models.IntegerField()
    constructor = models.CharField(max_length=50)
    laps = models.IntegerField()
    circuitID = models.CharField(max_length=50)


