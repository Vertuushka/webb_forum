# Generated by Django 5.0.1 on 2024-04-29 10:18

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
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 12, 18, 37, 299715)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 12, 18, 37, 299715)),
        ),
    ]
