# Generated by Django 5.0.4 on 2024-05-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_remove_alerts_latitude_remove_alerts_longitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.CharField(blank=True, max_length=288, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='test_models2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.CharField(blank=True, max_length=288, null=True)),
            ],
        ),
    ]