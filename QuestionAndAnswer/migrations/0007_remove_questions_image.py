# Generated by Django 2.1.7 on 2019-04-26 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAndAnswer', '0006_imagesquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='image',
        ),
    ]
