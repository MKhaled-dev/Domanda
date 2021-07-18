# Generated by Django 2.1.7 on 2019-04-26 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAndAnswer', '0005_auto_20190425_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagesQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='questionImage/')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.questions')),
            ],
        ),
    ]
