# Generated by Django 5.0.1 on 2024-04-25 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_warnings_history_time_warned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warnings_history',
            name='time_warned',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 21, 42, 25, 507636)),
        ),
    ]
