# Generated by Django 4.0.7 on 2022-09-30 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0022_level_role_levels'),
        ('quizes', '0023_remove_quiz_levels_quiz_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.level'),
        ),
    ]
