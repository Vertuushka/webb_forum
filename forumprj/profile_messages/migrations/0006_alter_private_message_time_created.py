# Generated by Django 4.2.5 on 2024-05-07 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_messages', '0005_alter_private_message_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private_message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 9, 35, 25, 112269)),
        ),
    ]
