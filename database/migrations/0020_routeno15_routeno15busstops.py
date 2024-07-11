# Generated by Django 5.0.4 on 2024-07-05 06:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_alter_noidaextentoincedointellectstops_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteNo15',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, dim=4, null=True, srid=4326)),
            ],
            options={
                'db_table': 'route no_15',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RouteNo15BusStops',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, dim=4, null=True, srid=4326)),
            ],
            options={
                'db_table': 'route no_15_bus stops',
                'managed': False,
            },
        ),
    ]