# Generated by Django 5.0.1 on 2024-04-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0008_alter_report_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_created',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
