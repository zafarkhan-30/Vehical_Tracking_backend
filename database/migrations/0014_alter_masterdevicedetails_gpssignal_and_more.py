# Generated by Django 5.0.4 on 2024-06-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_alter_masterdevicedetails_altitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdevicedetails',
            name='gpsSignal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='masterdevicedetails',
            name='heading',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='masterdevicedetails',
            name='odometer',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='masterdevicedetails',
            name='speedKph',
            field=models.IntegerField(null=True),
        ),
    ]