# Generated by Django 5.0.1 on 2024-05-13 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0052_thread_time_changed_alter_message_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 19, 42, 3, 503656)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 19, 42, 3, 502628)),
        ),
    ]