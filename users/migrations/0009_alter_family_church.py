# Generated by Django 4.0.7 on 2022-09-13 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_social_facebook_profile_social_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='church',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.church'),
        ),
    ]
