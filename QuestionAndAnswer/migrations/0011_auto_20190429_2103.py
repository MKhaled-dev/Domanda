# Generated by Django 2.1.7 on 2019-04-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAndAnswer', '0010_auto_20190429_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='bestanswer',
            field=models.BooleanField(default=0),
        ),
    ]