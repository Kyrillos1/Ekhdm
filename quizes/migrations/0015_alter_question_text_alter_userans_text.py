# Generated by Django 4.0.7 on 2022-09-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0014_userans_grade_alter_userans_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userans',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]