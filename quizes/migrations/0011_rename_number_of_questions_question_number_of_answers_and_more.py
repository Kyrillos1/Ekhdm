# Generated by Django 4.0.7 on 2022-09-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0010_rename_questionimage_question_question_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='number_of_questions',
            new_name='number_of_answers',
        ),
        migrations.AddField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]