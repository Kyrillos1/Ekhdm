# Generated by Django 4.0.7 on 2022-09-26 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0021_remove_quiz_level_quiz_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='level',
            new_name='levels',
        ),
    ]
