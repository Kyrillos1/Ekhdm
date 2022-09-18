# Generated by Django 4.0.7 on 2022-09-17 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_task_task_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submit',
            old_name='desc',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='submit',
            old_name='subject',
            new_name='remark',
        ),
        migrations.RemoveField(
            model_name='submit',
            name='task_file',
        ),
        migrations.AddField(
            model_name='submit',
            name='submitFile',
            field=models.FileField(blank=True, default='', null=True, upload_to='profiles/'),
        ),
        migrations.AddField(
            model_name='submit',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]