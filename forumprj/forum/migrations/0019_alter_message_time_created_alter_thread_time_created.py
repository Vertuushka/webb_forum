# Generated by Django 5.0.1 on 2024-04-25 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_alter_message_time_created_alter_thread_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 21, 18, 31, 536550)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 21, 18, 31, 536550)),
        ),
    ]
