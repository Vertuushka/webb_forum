# Generated by Django 5.0.1 on 2024-04-26 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0004_report_reason_alter_report_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='notification',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 21, 36, 33, 32086)),
        ),
    ]