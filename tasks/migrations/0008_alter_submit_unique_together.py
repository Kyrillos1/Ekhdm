# Generated by Django 4.1.1 on 2022-09-18 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_short_into_profile_short_intro'),
        ('tasks', '0007_rename_desc_submit_answer_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submit',
            unique_together={('user', 'task')},
        ),
    ]
