# Generated by Django 4.0.7 on 2022-09-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_book_file_book_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='book',
            name='bookFile',
            field=models.FileField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]
