# Generated by Django 4.2.5 on 2024-05-07 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_messages', '0004_alter_private_message_dialog_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private_message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 9, 34, 9, 141780)),
        ),
    ]