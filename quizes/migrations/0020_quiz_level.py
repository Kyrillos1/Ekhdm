# Generated by Django 4.0.7 on 2022-09-26 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_level_remove_profile_family_remove_profile_role_and_more'),
        ('quizes', '0019_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.level'),
        ),
    ]
