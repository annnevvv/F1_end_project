# Generated by Django 4.2.1 on 2023-05-31 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statisticsapp', '0004_delete_constructors_remove_driver_constructorid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('circuitID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Constructor',
            fields=[
                ('constructorID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driverID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('driver', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=20)),
                ('constructorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statisticsapp.constructor')),
            ],
        ),
        migrations.CreateModel(
            name='DriverStanding',
            fields=[
                ('ds_ID', models.AutoField(primary_key=True, serialize=False)),
                ('points', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('driverID', models.CharField(max_length=30)),
                ('constructorID', models.CharField(max_length=50)),
                ('constructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statisticsapp.constructor')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statisticsapp.driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverResult',
            fields=[
                ('dr_id', models.AutoField(primary_key=True, serialize=False)),
                ('driverID', models.CharField(max_length=30)),
                ('position', models.IntegerField()),
                ('points', models.IntegerField()),
                ('constructorID', models.CharField(max_length=50)),
                ('laps', models.IntegerField()),
                ('circuitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statisticsapp.circuit')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statisticsapp.driver')),
            ],
        ),
    ]
