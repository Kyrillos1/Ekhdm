# Generated by Django 4.0.7 on 2022-09-16 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0006_alter_quiz_valid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='topic',
        ),
    ]
