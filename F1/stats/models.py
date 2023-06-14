from django.db import models

# Create your models here.
from django.db import models
from datetime import date

# Create your models here.
from django.db import models
from django.db.models import Min


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Circuits(models.Model):
    circuitid = models.CharField(db_column='circuitID',max_length=2, primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'circuits'

    @classmethod
    def get_upcoming_races(cls):
        today = date.today()
        next_race_date = cls.objects.filter(date__gt=today).aggregate(Min('date'))['date__min']
        return cls.objects.filter(date=next_race_date)


class Constructors(models.Model):
    constructorid = models.CharField(db_column='constructorID', primary_key=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'constructors'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DriverStandings(models.Model):
    ds_id = models.AutoField(db_column='ds_ID', primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='driverID')  # Field name made lowercase.
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING, db_column='constructorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'driver_standings'



class ConstructorStandings(models.Model):
    cs_id = models.AutoField(db_column='cs_ID', primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING, db_column='constructorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'constructor_standings'



class Drivers(models.Model):
    driverid = models.CharField(db_column='driverID', primary_key=True, max_length=30)  # Field name made lowercase.
    driver = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING, db_column='constructorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drivers'


class DriversResults(models.Model):
    dr_id = models.AutoField(primary_key=True)
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driverID')  # Field name made lowercase.
    position = models.IntegerField()
    points = models.IntegerField()
    constructorid = models.ForeignKey(Constructors,models.DO_NOTHING,db_column='constructorID', max_length=50)  # Field name made lowercase.
    laps = models.IntegerField()
    circuitid = models.ForeignKey(Circuits, models.DO_NOTHING, db_column='circuitID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drivers_results'
    @classmethod
    def get_last_race(cls):
        return cls.objects.aggregate(max_circuitid=models.Max('circuitid'))['max_circuitid']

class StatsDriverresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    driverid = models.CharField(db_column='driverID', max_length=30)  # Field name made lowercase.
    driver = models.CharField(max_length=30)
    position = models.IntegerField()
    points = models.IntegerField()
    constructor = models.CharField(max_length=50)
    laps = models.IntegerField()
    circuitid = models.CharField(db_column='circuitID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stats_driverresult'

