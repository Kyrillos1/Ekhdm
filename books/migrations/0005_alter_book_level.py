# Generated by Django 4.0.7 on 2022-09-30 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0022_level_role_levels'),
        ('books', '0004_book_level_book_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.level'),
        ),
    ]
