# Generated by Django 4.2.7 on 2023-12-04 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0004_profile_username_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username_verified',
        ),
    ]