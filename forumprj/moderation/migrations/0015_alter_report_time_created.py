# Generated by Django 5.0.1 on 2024-04-30 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0014_alter_report_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 11, 42, 28, 779296)),
        ),
    ]
