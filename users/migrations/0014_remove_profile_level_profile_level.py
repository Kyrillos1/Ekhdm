# Generated by Django 4.0.7 on 2022-09-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_level_remove_profile_family_remove_profile_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='level',
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.ManyToManyField(blank=True, null=True, to='users.level'),
        ),
    ]