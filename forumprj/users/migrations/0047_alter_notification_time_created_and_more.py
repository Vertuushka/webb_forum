# Generated by Django 5.0.1 on 2024-05-07 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_alter_notification_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 19, 38, 45, 536933)),
        ),
        migrations.AlterField(
            model_name='warnings_history',
            name='time_warned',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 19, 38, 45, 535932)),
        ),
    ]
