# Generated by Django 4.2.5 on 2024-05-07 06:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_messages', '0002_private_message_is_read_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private_message',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 8, 53, 31, 888948)),
        ),
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog_user_1', to=settings.AUTH_USER_MODEL)),
                ('user_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog_user_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='private_message',
            name='dialog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_messages.dialog'),
        ),
    ]
