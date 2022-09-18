# Generated by Django 4.0.7 on 2022-09-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_church_family_rename_location_profile_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('Makhdom', 'مخدوم'), ('Khadm', 'خادم'), ('Family_head', 'امين اسرة'), ('Priest', 'قس'), ('Archpriest', 'قمص')], max_length=15, null=True),
        ),
    ]
