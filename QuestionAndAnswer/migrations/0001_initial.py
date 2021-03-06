# Generated by Django 2.1.7 on 2019-04-25 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badages', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('answer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='answerImage/')),
                ('bestanswer', models.BooleanField()),
                ('mentioned_users', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='change_theme',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('theme_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('comment_time', models.TimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.answer')),
            ],
        ),
        migrations.CreateModel(
            name='followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='liked_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.answer')),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification_content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('event_number', models.IntegerField()),
                ('event_title', models.CharField(max_length=1)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('vote', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='questionImage/')),
                ('views', models.IntegerField(default=0)),
                ('turnoffcomment', models.BooleanField(default=False)),
                ('num_answers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='saved_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.questions')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='profileImage')),
                ('country', models.CharField(max_length=50)),
                ('career_type', models.CharField(max_length=100)),
                ('career_value', models.CharField(max_length=100)),
                ('GitHubLink', models.URLField(max_length=150)),
                ('TwitterLink', models.URLField(max_length=150)),
                ('WebsiteLink', models.URLField(max_length=150)),
                ('aboutme', models.TextField()),
                ('workORschool', models.CharField(max_length=6)),
                ('notifiy_count', models.IntegerField()),
                ('number_followers', models.IntegerField()),
                ('interests', models.CharField(default='0,0,0,0', max_length=50)),
                ('ua', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='viewed_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.questions')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users')),
            ],
        ),
        migrations.CreateModel(
            name='voted_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_up', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.questions')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users')),
            ],
        ),
        migrations.AddField(
            model_name='saved_question',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users'),
        ),
        migrations.AddField(
            model_name='questions',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuestionAndAnswer.users'),
        ),
        migrations.AddField(
            model_name='notification',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users'),
        ),
        migrations.AddField(
            model_name='liked_answers',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users'),
        ),
        migrations.AddField(
            model_name='followers',
            name='followed_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users'),
        ),
        migrations.AddField(
            model_name='category',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.questions'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.questions'),
        ),
        migrations.AddField(
            model_name='answer',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users'),
        ),
        migrations.AddField(
            model_name='achievements',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionAndAnswer.users'),
        ),
        migrations.AlterUniqueTogether(
            name='voted_questions',
            unique_together={('question', 'username')},
        ),
        migrations.AlterUniqueTogether(
            name='viewed_questions',
            unique_together={('question', 'username')},
        ),
        migrations.AlterUniqueTogether(
            name='liked_answers',
            unique_together={('answer', 'username')},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('categoryname', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='achievements',
            unique_together={('username', 'badages')},
        ),
    ]
