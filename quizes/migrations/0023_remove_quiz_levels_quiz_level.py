# Generated by Django 4.0.7 on 2022-09-26 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_rename_level_profile_levels'),
        ('quizes', '0022_rename_level_quiz_levels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='levels',
        ),
        migrations.AddField(
            model_name='quiz',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.level'),
        ),
    ]