# Generated by Django 4.0.7 on 2022-09-16 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_options_alter_task_task_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_image',
        ),
    ]
