# Generated by Django 4.2.5 on 2024-04-26 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0023_alter_message_time_created_alter_thread_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 9, 9, 27, 641368)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 9, 9, 27, 641368)),
        ),
    ]