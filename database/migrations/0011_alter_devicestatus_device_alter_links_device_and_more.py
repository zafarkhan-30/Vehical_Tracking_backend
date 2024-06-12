# Generated by Django 5.0.4 on 2024-06-12 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_alter_masterdevicedetails_alert_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicestatus',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deviceStatus', to='database.devices'),
        ),
        migrations.AlterField(
            model_name='links',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_links', to='database.devices'),
        ),
        migrations.AlterField(
            model_name='masterdevicedetails',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_device_id', to='database.devices'),
        ),
        migrations.AlterField(
            model_name='todaysdrive',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_todaysDrive', to='database.devices'),
        ),
    ]