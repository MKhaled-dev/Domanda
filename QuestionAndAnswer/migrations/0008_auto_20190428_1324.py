# Generated by Django 2.1.7 on 2019-04-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAndAnswer', '0007_remove_questions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='number_followers',
            field=models.IntegerField(default=0),
        ),
    ]