# Generated by Django 4.1 on 2022-09-11 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment_userid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]