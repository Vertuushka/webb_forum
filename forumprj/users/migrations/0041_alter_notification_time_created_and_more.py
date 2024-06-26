# Generated by Django 4.2.5 on 2024-05-07 07:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_messages', '0006_alter_private_message_time_created'),
        ('forum', '0044_alter_message_time_created_alter_thread_time_created'),
        ('users', '0040_rename_content_warnings_history_forum_msg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 9, 35, 25, 113269)),
        ),
        migrations.AlterField(
            model_name='warnings_history',
            name='forum_msg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.message'),
        ),
        migrations.AlterField(
            model_name='warnings_history',
            name='profile_msg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_messages.private_message'),
        ),
        migrations.AlterField(
            model_name='warnings_history',
            name='time_warned',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 9, 35, 25, 113269)),
        ),
    ]
