# Generated by Django 4.2.5 on 2024-05-07 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_alter_notification_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 10, 34, 5, 156293)),
        ),
        migrations.AlterField(
            model_name='warnings_history',
            name='time_warned',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 10, 34, 5, 156293)),
        ),
    ]
