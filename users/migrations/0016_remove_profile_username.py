# Generated by Django 4.0.7 on 2022-09-26 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
