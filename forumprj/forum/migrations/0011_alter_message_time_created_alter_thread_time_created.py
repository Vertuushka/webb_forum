# Generated by Django 4.2.5 on 2024-04-25 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_alter_message_time_created_alter_thread_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 11, 24, 57, 693075)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 11, 24, 57, 693075)),
        ),
    ]