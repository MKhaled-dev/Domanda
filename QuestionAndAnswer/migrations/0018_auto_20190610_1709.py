# Generated by Django 2.1.7 on 2019-06-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAndAnswer', '0017_auto_20190505_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
