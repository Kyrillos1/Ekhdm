# Generated by Django 4.0.7 on 2022-09-26 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='level',
            new_name='levels',
        ),
    ]
