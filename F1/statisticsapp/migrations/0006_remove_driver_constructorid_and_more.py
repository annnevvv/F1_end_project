# Generated by Django 4.2.1 on 2023-06-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsapp', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='constructorID',
        ),
        migrations.RemoveField(
            model_name='driverstanding',
            name='constructor',
        ),
        migrations.RemoveField(
            model_name='driverstanding',
            name='driver',
        ),
        migrations.RenameField(
            model_name='driverresult',
            old_name='constructorID',
            new_name='constructor',
        ),
        migrations.RemoveField(
            model_name='driverresult',
            name='dr_id',
        ),
        migrations.AddField(
            model_name='driverresult',
            name='id',
            field=models.BigAutoField(auto_created=True, default='abcd', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driverresult',
            name='circuitID',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='driverresult',
            name='driver',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Circuit',
        ),
        migrations.DeleteModel(
            name='Constructor',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='DriverStanding',
        ),
    ]
