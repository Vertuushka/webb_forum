# Generated by Django 5.0.1 on 2024-04-30 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0026_node_staff_only_alter_message_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 10, 38, 56, 208187)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='msg_amount',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 10, 38, 56, 208187)),
        ),
    ]
