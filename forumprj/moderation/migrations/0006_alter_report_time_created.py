# Generated by Django 5.0.1 on 2024-04-26 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0005_alter_report_notification_alter_report_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 22, 27, 6, 159594)),
        ),
    ]
