# Generated by Django 4.0.7 on 2022-09-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_alter_note_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='am',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='holy_communion',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='liturgy',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='pm',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='read_bible',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
