from django.db import models
from django.contrib.auth.models import User

# Start User Model
class users(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 50)
    profile_image = models.ImageField(upload_to = 'profileImage')
    country = models.CharField(max_length = 50)
    career_type = models.CharField(max_length = 100)
    career_value = models.CharField(max_length = 100)
    GitHubLink = models.URLField(max_length = 150)
    TwitterLink = models.URLField(max_length = 150)
    WebsiteLink = models.URLField(max_length = 150)
    aboutme = models.TextField()
    workORschool = models.CharField(max_length = 6)
    notifiy_count = models.IntegerField()
    achievement_count = models.IntegerField(default = 0)
    number_followers = models.IntegerField(default = 0)
    interests = models.CharField(max_length = 50, default = '0,0,0,0')
    verify_code = models.CharField(max_length = 10, default = "verify")
    verified = models.BooleanField(default = 0)
    theme_path = models.TextField(default = "/static/QuestionAndAnswer/css/themes/default-theme.css")
    mode_path = models.TextField(default = "dark")  #/static/QuestionAndAnswer/css/modes/dark-mode.css
    ua = models.OneToOneField(User, on_delete = models.CASCADE)


# Start achievements Model
class achievements(models.Model):
    username = models.ForeignKey(users, on_delete= models.CASCADE)
    achievement = models.CharField(max_length = 50)


# Start Followers Model
class followers(models.Model):
    followed_user = models.ForeignKey(users, on_delete= models.CASCADE)
    follower = models.CharField(max_length = 50)



# Start Notifications Model
class notification(models.Model):
    notification_id = models.AutoField(primary_key = True)
    notification_content = models.TextField()
    date = models.DateField(auto_now_add = True)
    time = models.TimeField(auto_now_add = True)
    event_number = models.IntegerField()
    event_title = models.CharField(max_length = 1)
    seen = models.BooleanField(default = False)
    username = models.ForeignKey(users, on_delete= models.CASCADE)

    
    def sub_notification_content(self):
        if len(self.notification_content) > 55:
            return self.notification_content[:55] + '...'
        else:
            return self.notification_content


# Start Questions Model
class questions(models.Model):
    question_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    vote = models.IntegerField(default = 0)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    views = models.IntegerField(default = 0)
    turnoffcomment = models.BooleanField(default = False)
    num_answers = models.IntegerField(default = 0)
    username = models.ForeignKey(users, on_delete= models.SET_NULL, null = True)

    def sub_content_home(self):
        if len(self.title) > 80:
            return self.title[:80] + ' ...'
        else:
            return self.title


# Start Images for Questions
class imagesQuestion(models.Model):
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'questionImage/', blank = True, null = True)



# Start Answers Model
class answer(models.Model):
    answer_id = models.AutoField(primary_key = True)
    content = models.TextField()
    likes = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = 'answerImage/')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    bestanswer = models.IntegerField(default = 0)
    username = models.ForeignKey(users, on_delete= models.CASCADE)
    question = models.ForeignKey(questions, on_delete=models.CASCADE)


    def answer_content(self):
        if len(self.content) > 50:
            return self.content[:50] + '...'
        else:
            return self.content


# Start Likes Table
class liked_answers(models.Model):
    answer = models.ForeignKey(answer, on_delete=models.CASCADE)
    username = models.ForeignKey(users, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("answer", "username")



# Start Category Model
class category(models.Model):
    categoryname = models.CharField(max_length = 250)
    question = models.ForeignKey(questions, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("categoryname", "question")



# Start Viewed Questions
class viewed_questions(models.Model):
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    username = models.ForeignKey(users, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("question", "username")




# Start Comments Class
class comments(models.Model):
    answer = models.ForeignKey(answer, on_delete = models.CASCADE)
    comment_content = models.TextField()
    comment_date = models.DateField(auto_now_add = True)
    comment_time = models.TimeField(auto_now_add = True)
    comment_user = models.ForeignKey(users, on_delete = models.CASCADE)



# Start Voting Comments
class voted_questions(models.Model):
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    username = models.ForeignKey(users, on_delete=models.CASCADE)
    vote_up = models.BooleanField(default = False)

    class Meta:
        unique_together = ("question", "username")
    


# Start Saved Questions
class saved_question(models.Model):
    saved_question = models.ForeignKey(questions, on_delete = models.CASCADE)
    username = models.ForeignKey(users, on_delete = models.CASCADE)