# Generated by Django 5.1.1 on 2024-09-17 14:49

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('sport', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2024, 9, 17, 14, 49, 13, 94577, tzinfo=datetime.timezone.utc))),
                ('tournament_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('tournament_end', models.DateTimeField(default=datetime.datetime(2024, 9, 22, 14, 49, 13, 94706, tzinfo=datetime.timezone.utc))),
                ('bracketing_system', models.CharField(max_length=255)),
            ],
        ),
    ]