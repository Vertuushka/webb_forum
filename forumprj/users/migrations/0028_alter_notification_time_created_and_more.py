# Generated by Django 5.0.1 on 2024-05-05 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_notification_time_created_alter_profile_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 11, 38, 21, 605811)),
        ),
        migrations.AlterField(
            model_name='warnings_history',
            name='time_warned',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 11, 38, 21, 604771)),
        ),
    ]
