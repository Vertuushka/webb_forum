# Generated by Django 4.2.5 on 2024-05-13 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_messages', '0013_alter_private_message_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private_message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 9, 53, 23, 643578)),
        ),
    ]
