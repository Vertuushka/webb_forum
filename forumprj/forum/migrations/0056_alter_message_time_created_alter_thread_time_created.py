# Generated by Django 5.0.6 on 2024-05-23 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0055_message_changer_alter_message_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 23, 13, 22, 11, 797691)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 23, 13, 22, 11, 796695)),
        ),
    ]