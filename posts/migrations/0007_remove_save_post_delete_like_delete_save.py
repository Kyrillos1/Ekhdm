# Generated by Django 4.1 on 2022-09-11 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='save',
            name='post',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Save',
        ),
    ]
