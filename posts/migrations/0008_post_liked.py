# Generated by Django 4.1 on 2022-09-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_options'),
        ('posts', '0007_remove_save_post_delete_like_delete_save'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='users.profile'),
        ),
    ]
