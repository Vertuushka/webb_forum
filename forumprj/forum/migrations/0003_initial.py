# Generated by Django 4.2.5 on 2024-04-22 08:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('type_question', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.node')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_pinned', models.BooleanField(default=False)),
                ('time_created', models.DateTimeField(default=datetime.datetime(2024, 4, 22, 10, 34, 8, 895500))),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.node')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('upvotes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('downvotes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('is_solution', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(default=datetime.datetime(2024, 4, 22, 10, 34, 8, 896111))),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=225)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.message')),
            ],
        ),
    ]