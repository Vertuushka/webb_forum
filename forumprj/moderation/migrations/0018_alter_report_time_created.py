# Generated by Django 5.0.1 on 2024-05-05 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0017_alter_report_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 11, 44, 33, 933354)),
        ),
    ]