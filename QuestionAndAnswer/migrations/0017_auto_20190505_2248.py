# Generated by Django 2.1.7 on 2019-05-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAndAnswer', '0016_auto_20190502_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mode_path',
            field=models.TextField(default='dark'),
        ),
    ]
