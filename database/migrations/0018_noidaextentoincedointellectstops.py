# Generated by Django 5.0.4 on 2024-06-26 09:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_noidaextentoincedointellectroute'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoidaExtenToIncedointellectStops',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('descriptio', models.CharField(blank=True, max_length=254, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=24, null=True)),
                ('begin', models.CharField(blank=True, max_length=24, null=True)),
                ('end', models.CharField(blank=True, max_length=24, null=True)),
                ('altitudemo', models.CharField(blank=True, max_length=254, null=True)),
                ('tessellate', models.FloatField(blank=True, null=True)),
                ('extrude', models.FloatField(blank=True, null=True)),
                ('visibility', models.FloatField(blank=True, null=True)),
                ('draworder', models.FloatField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=254, null=True)),
                ('latitude', models.CharField(blank=True, max_length=254, null=True)),
                ('longitude', models.CharField(blank=True, max_length=254, null=True)),
                ('english_ne', models.CharField(blank=True, max_length=254, null=True)),
                ('english_se', models.CharField(blank=True, max_length=254, null=True)),
                ('local_neig', models.CharField(blank=True, max_length=254, null=True)),
                ('local_prim', models.CharField(blank=True, max_length=254, null=True)),
                ('local_seco', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, dim=4, null=True, srid=4326)),
            ],
            options={
                'db_table': 'noida exten_to_incedointellect_stops',
                'managed': False,
            },
        ),
    ]