# Generated by Django 5.0.4 on 2024-07-10 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_routeno15_routeno15busstops'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caninfo',
            name='device',
        ),
        migrations.RemoveField(
            model_name='devicelocation',
            name='device',
        ),
        migrations.RemoveField(
            model_name='devicestatus',
            name='device',
        ),
        migrations.RemoveField(
            model_name='dinputs',
            name='device',
        ),
        migrations.RemoveField(
            model_name='links',
            name='device',
        ),
        migrations.RemoveField(
            model_name='todaysdrive',
            name='device',
        ),
        migrations.DeleteModel(
            name='alerts',
        ),
        migrations.DeleteModel(
            name='canInfo',
        ),
        migrations.DeleteModel(
            name='deviceLocation',
        ),
        migrations.DeleteModel(
            name='deviceStatus',
        ),
        migrations.DeleteModel(
            name='dinputs',
        ),
        migrations.DeleteModel(
            name='links',
        ),
        migrations.DeleteModel(
            name='todaysDrive',
        ),
    ]
