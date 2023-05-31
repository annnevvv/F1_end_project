from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


from django.db import models

class Constructor(models.Model):
    constructorID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)

class Driver(models.Model):
    driverID = models.CharField(max_length=30, primary_key=True)
    driver = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    constructorID = models.ForeignKey(Constructor, on_delete=models.CASCADE)

class Circuit(models.Model):
    circuitID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    date = models.DateField()

class DriverResult(models.Model):
    dr_id = models.AutoField(primary_key=True)
    driverID = models.CharField(max_length=30)
    position = models.IntegerField()
    points = models.IntegerField()
    constructorID = models.CharField(max_length=50)
    laps = models.IntegerField()
    circuitID = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class DriverStanding(models.Model):
    ds_ID = models.AutoField(primary_key=True)
    points = models.IntegerField()
    wins = models.IntegerField()
    driverID = models.CharField(max_length=30)
    constructorID = models.CharField(max_length=50)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)



