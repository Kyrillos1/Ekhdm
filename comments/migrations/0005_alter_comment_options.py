# Generated by Django 4.0.7 on 2022-09-16 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_post_alter_like_post_alter_save_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
    ]