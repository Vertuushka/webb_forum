# Generated by Django 5.0.1 on 2024-04-27 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_title_alter_warnings_history_time_warned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warnings_history',
            name='time_warned',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 20, 7, 30, 78574)),
        ),
    ]