# Generated by Django 5.0.1 on 2024-05-05 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0031_message_deleted_by_alter_message_time_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time_changed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 11, 44, 33, 931362)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 11, 44, 33, 930326)),
        ),
    ]
