# Generated by Django 4.2.1 on 2023-05-31 14:54

from django.db import migrations

trigger1 = """
CREATE TRIGGER update_points AFTER INSERT ON DriverResult FOR EACH ROW
BEGIN
    UPDATE DriverStanding ds
    INNER JOIN (SELECT driverID, SUM(points) AS total FROM DriverResult GROUP BY driverID) x ON ds.driverID = x.driverID
    SET ds.points = x.total;
END;
"""

trigger2 = """
CREATE TRIGGER wins AFTER INSERT ON driver_results FOR EACH ROW
BEGIN
    UPDATE DriverStanding ds
    INNER JOIN (
        SELECT driverID, SUM(position = 1) AS wins FROM DriverResult GROUP BY driverID
    ) x ON ds.driverID = x.driverID
    SET ds.wins = x.wins;
END;
"""

class Migration(migrations.Migration):

    dependencies = [
        ('statisticsapp', '0002_circuit_constructor_driver_driverresult_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql=trigger1,
            reverse_sql=migrations.RunSQL.noop
        ),
        migrations.RunSQL(
            sql=trigger2,
            reverse_sql=migrations.RunSQL.noop
        ),
    ]