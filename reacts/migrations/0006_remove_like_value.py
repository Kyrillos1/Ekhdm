# Generated by Django 4.0.7 on 2022-09-23 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reacts', '0005_alter_comment_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
    ]
