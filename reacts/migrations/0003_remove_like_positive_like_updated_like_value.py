# Generated by Django 4.1 on 2022-09-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reacts', '0002_save_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='positive',
        ),
        migrations.AddField(
            model_name='like',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=8, null=True),
        ),
    ]
