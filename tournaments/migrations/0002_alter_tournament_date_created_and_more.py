# Generated by Django 5.1.1 on 2024-10-30 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 30, 14, 28, 18, 648925, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament_end',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 14, 28, 18, 649042, tzinfo=datetime.timezone.utc)),
        ),
    ]