# Generated by Django 5.1.1 on 2024-10-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_banner',
            field=models.ImageField(default='defaults/default_profile.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='defaults/default_profile.jpg', upload_to='images/'),
        ),
    ]