# Generated by Django 4.1.1 on 2022-09-18 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0007_remove_quiz_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='name',
            new_name='title',
        ),
    ]