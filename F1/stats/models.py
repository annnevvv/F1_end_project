from datetime import date


from django.db import models
from django.db.models import Min



class Circuits(models.Model):
    circuitid = models.CharField(db_column='circuitID',
                                 max_length=2,
                                 primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = 'circuits'

    @classmethod
    def get_upcoming_races(cls):
        today = date.today()
        next_race_date = \
        cls.objects.filter(date__gt=today).aggregate(Min('date'))['date__min']
        return cls.objects.filter(date=next_race_date)


class Constructors(models.Model):
    constructorid = models.CharField(db_column='constructorID',
                                     primary_key=True,
                                     max_length=15)  # Field name made lowercase.
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'constructors'



class DriverStandings(models.Model):
    ds_id = models.AutoField(db_column='ds_ID',
                             primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, null=True,
                                 db_column='driverID')  # Field name made lowercase.
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING, null=True,
                                      db_column='constructorID')  # Field name made lowercase.

    class Meta:
        db_table = 'driver_standings'


class ConstructorStandings(models.Model):
    cs_id = models.AutoField(db_column='cs_ID',
                             primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING, null=True,
                                      db_column='constructorID')  # Field name made lowercase.

    class Meta:
        db_table = 'constructor_standings'


class Drivers(models.Model):
    driverid = models.CharField(db_column='driverID', primary_key=True,
                                max_length=30)  # Field name made lowercase.
    driver = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING,null=True,
                                      db_column='constructorID')  # Field name made lowercase.

    class Meta:
        db_table = 'drivers'


class DriversResults(models.Model):
    dr_id = models.AutoField(primary_key=True)
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING,null=True,
                                 db_column='driverID')  # Field name made lowercase.
    position = models.IntegerField()
    points = models.IntegerField()
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING,null=True,
                                      db_column='constructorID',
                                      max_length=50)  # Field name made lowercase.
    laps = models.IntegerField()
    circuitid = models.ForeignKey(Circuits, models.DO_NOTHING,null=True,
                                  db_column='circuitID')  # Field name made lowercase.

    class Meta:
        db_table = 'drivers_results'

    @classmethod
    def get_last_race(cls):
        return cls.objects.aggregate(max_circuitid=models.Max('circuitid'))[
            'max_circuitid']


class StatsDriverresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    driverid = models.CharField(db_column='driverID',
                                max_length=30)  # Field name made lowercase.
    driver = models.CharField(max_length=30)
    position = models.IntegerField()
    points = models.IntegerField()
    constructor = models.CharField(max_length=50)
    laps = models.IntegerField()
    circuitid = models.CharField(db_column='circuitID',
                                 max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'stats_driverresult'
