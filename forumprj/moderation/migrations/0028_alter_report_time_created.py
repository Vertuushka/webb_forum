# Generated by Django 4.2.5 on 2024-05-07 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0027_alter_report_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 8, 54, 46, 128991)),
        ),
    ]
