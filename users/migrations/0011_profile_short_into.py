# Generated by Django 4.0.7 on 2022-09-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_social_facebook_church_social_facebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='short_into',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]