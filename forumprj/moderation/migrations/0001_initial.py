# Generated by Django 4.2.5 on 2024-04-25 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0015_alter_message_time_created_alter_thread_time_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_closed', models.BooleanField(default=False)),
                ('is_declined', models.BooleanField(default=False)),
                ('is_resolved', models.BooleanField(default=False)),
                ('assigned', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned', to=settings.AUTH_USER_MODEL)),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.message')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
