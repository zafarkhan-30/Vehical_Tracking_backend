# Generated by Django 5.0.4 on 2024-05-28 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_alerts_latitude_alter_alerts_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerts',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='alerts',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='devicelocation',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='devicelocation',
            name='longitude',
        ),
    ]