from django.shortcuts import render, render_to_response
from QuestionAndAnswer import models, forms
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib import messages

import email
from shutil import copyfile
import os
import shutil
import string
import random

import datetime
from datetime import timedelta
import pickle
from random import shuffle
from QuestionAndAnswer.classification import preprocess


question_content = ''

# 
def searchAchievements(_achievement, listOfAchievements):
    for achievement in listOfAchievements:
        if achievement.achievement == _achievement:
            return False
    return True

def rewardingAchievements(userID, typeOfAction):
    user = models.users.objects.get(username = userID)

    try:
        listOfAchievements = models.achievements.objects.filter(username = user.username)

        if typeOfAction == 0: #Asking Question
            if searchAchievements("First Question!", listOfAchievements):
                numOfQuestions = models.questions.objects.filter(username = user).count()
                if numOfQuestions == 1:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "First Question!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("5th Question!", listOfAchievements):
                numOfQuestions = models.questions.objects.filter(username = user).count()
                if numOfQuestions == 5:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "5th Question!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("10th Question!", listOfAchievements):
                numOfQuestions = models.questions.objects.filter(username = user).count()
                if numOfQuestions == 10:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "10th Question!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("25th Question!", listOfAchievements):
                numOfQuestions = models.questions.objects.filter(username = user).count()
                if numOfQuestions == 25:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "25th Question!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("50th Question!", listOfAchievements):
                numOfQuestions = models.questions.objects.filter(username = user).count()
                if numOfQuestions == 50:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "50th Question!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("100th Question!", listOfAchievements):
                numOfQuestions = models.questions.objects.filter(username = user).count()
                if numOfQuestions == 100:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "100th Question!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

        elif typeOfAction == 1: #Answering Question
            if searchAchievements("First Answer!", listOfAchievements):
                numOfAnswers = models.answer.objects.filter(username = user).count()
                if numOfAnswers == 1:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "First Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("5th Answer!", listOfAchievements):
                numOfAnswers = models.answer.objects.filter(username = user).count()
                if numOfAnswers == 5:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "5th Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("10th Answer!", listOfAchievements):
                numOfAnswers = models.answer.objects.filter(username = user).count()
                if numOfAnswers == 10:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "10th Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("25th Answer!", listOfAchievements):
                numOfAnswers = models.answer.objects.filter(username = user).count()
                if numOfAnswers == 25:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "25th Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()


            elif searchAchievements("50th Answer!", listOfAchievements):
                numOfAnswers = models.answer.objects.filter(username = user).count()
                if numOfAnswers == 50:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "50th Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("100th Answer!", listOfAchievements):
                numOfAnswers = models.answer.objects.filter(username = user).count()
                if numOfAnswers == 100:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "100th Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

        elif typeOfAction == 2: #Completing Profile
            if searchAchievements("Profile Completed!", listOfAchievements):
                count = 0
                listOfAttributes = ['firstName', 'lastName', 'email', 'profile_image', 'country', 'career_type', 'career_value', 'GitHubLink',
                                    'TwitterLink', 'WebsiteLink', 'aboutme', 'workORschool']
                for attribute in listOfAttributes:
                    if getattr(user, attribute) != "":
                        count += 1

                if count == len(listOfAttributes):
                    newAchievement = models.achievements()
                    newAchievement.achievement = "Profile Completed!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

        elif typeOfAction == 3: #Best Answer
            if searchAchievements("Best Answer!", listOfAchievements):
                newAchievement = models.achievements()
                newAchievement.achievement = "Best Answer!"
                newAchievement.username = user
                newAchievement.save()

                # Add achievement count
                user.achievement_count += 1
                user.save()

            elif searchAchievements("5th Best Answer!", listOfAchievements):
                if models.answer.objects.filter(username = user.username, bestanswer = 1).count() == 5:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "5th Best Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("10th Best Answer!", listOfAchievements):
                if models.answer.objects.filter(username = user.username, bestanswer = 1).count() == 10:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "10th Best Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("25th Best Answer!", listOfAchievements):
                if models.answer.objects.filter(username = user.username, bestanswer = 1).count() == 25:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "25th Best Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("50th Best Answer!", listOfAchievements):
                if models.answer.objects.filter(username = user.username, bestanswer = 1).count() == 50:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "50th Best Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()

            elif searchAchievements("100th Best Answer!", listOfAchievements):
                if models.answer.objects.filter(username = user.username, bestanswer = 1).count() == 100:
                    newAchievement = models.achievements()
                    newAchievement.achievement = "100th Best Answer!"
                    newAchievement.username = user
                    newAchievement.save()

                    # Add achievement count
                    user.achievement_count += 1
                    user.save()
    except:
        pass    

# Start Help
def help(request):
    context = {
        'body':'body-background-img-color',
        'title':'Help',
    }
    return render(request, 'help.html', context)

# Function To Generate Random Verification Code
def random_code(limit = 6):
    random_string =""
    return random_string.join(random.choice(string.ascii_letters) for x in range(limit))

# Start Function For Return All Users
def all_user(request, username_char):
    all_users = models.users.objects.filter(username__contains = username_char)
    all_user_list = []
    data = {}

    for username in all_users:
        if request.user.username != username.username:
            all_user_list.append(username.username)

    data['all_user'] = all_user_list

    return JsonResponse(data)


# Start About Page
def about(request):
    return render(request, 'about.html', {'body':'body-background', 'title':'About'})


# Start Home Page
def home(request):
    try:
        del request.session['displayed_questions']

    except:
        pass

    displayed_questions = request.session.get('displayed_questions')

    if not displayed_questions:
        displayed_questions = 0

    questions_list = []
    questions_list_id = []
    number_of_questions = models.questions.objects.all().count()

    if number_of_questions == 0:
        return render(request, 'home.html', {'body':'body-background-img-color', 'title':'Home'})


    questions = models.questions.objects.all().order_by('-question_id')

    for i in questions:
        questions_list_id.append(i.question_id)

    i = 0
    count = 0
    while count < 8:
        try:
            questions_list.append(models.questions.objects.get(question_id = questions_list_id[i]))
            displayed_questions += 1
        except:
            break
        i += 1
        count += 1

    request.session['displayed_questions'] = displayed_questions

    all_category = models.category.objects.all()

    # Get Last Notification (question)
    last_notifiy = models.notification.objects.filter(event_title = 'q').last()
   
    context = {
        'body':'body-background-img-color',
        'title':'Home',
        'questions':questions_list,
        'lastquestion':questions_list[-1],
        'number_of_questions':number_of_questions,
        'displayed_questions':displayed_questions,
        'categories' : all_category,
        'lastNotification': last_notifiy,
    }
    
    return render(request, 'home.html', context)

# Start Ask Questions Page
@login_required(login_url = "/domanda/signin")
def ask_question(request):
    return render(request, 'question.html', {'body':'body-background-img-color', 'title':'Ask Question'})


# Post Question
def post_question(request, user_id):
    if request.method == "POST":
        user = models.users.objects.get(username = user_id)

        title = request.POST['question-title']
        content = request.POST['question-body']

        newQuestion = models.questions()
        newNotification = models.notification()

        newQuestion.title = title.lower()
        newQuestion.content = content
        newQuestion.username = user

        newQuestion.save()

        #Start get all followers and send notifications to them
        number_of_followers = models.followers.objects.filter(followed_user = user_id).count()

        if number_of_followers > 0:
            all_followers = models.followers.objects.filter(followed_user = user_id)

            for follower in all_followers:
                follower_notification = models.notification()

                follower_notification.notification_content = user_id
                follower_notification.event_number = newQuestion.question_id
                follower_notification.event_title = 'u'

                follower_user = models.users.objects.get(username = follower.follower)
                follower_notification.username = follower_user

                follower_user.notifiy_count += 1

                follower_user.save()
                follower_notification.save()
            

        #------------------------------------
        rewardingAchievements(user_id, 0) 
        #------------------------------------

        # Start save iamge for the new question
        question_form = forms.uploadQuestionImage(request.POST, request.FILES, instance = newQuestion)
        
        if question_form.is_valid():
            for img in request.FILES.getlist('image'):
                imgQuestion = models.imagesQuestion(question = newQuestion, image = img)
                imgQuestion.save()

            question_form.save()
        
        newNotification.notification_content = title
        newNotification.event_number = newQuestion.question_id
        newNotification.event_title = 'q'
        newNotification.username = user

        newNotification.save()

        # Change Count Number for Add New Question
        user.notifiy_count += 1
        user.save()


        # Display The First Thirty Letters In Question Title
        if len(title) >= 48:
            title_content = title[:30] + '...'
        else:
            title_content = title 
        
        messages.success(request, f'You posted a question : { title_content }')

        # Start Classification
        texts1 = [title]
        common_dot_words = ['U.S.', 'St.', 'Mr.', 'Mrs.', 'D.C.']
        test_text=preprocess(texts1,keep_list = common_dot_words,remove_stopwords = True,lemmatization =True,stemming=False,stem_type='PorterStemmer')
        loaded_model=pickle.load(open('m.sav', 'rb'))
        vectorizer=pickle.load(open('v.sav', 'rb'))

        test_text1=vectorizer.transform(test_text)
        result=loaded_model.predict(test_text1)
        x = result[0]

        arr=["World","Sport","Business","Science"]
        
        category = models.category()
        category.categoryname = arr[x - 1]
        category.question = newQuestion

        category.save()

    return HttpResponseRedirect('/')

    
# Get Question 
def get_question(request, question_id):
    question = models.questions.objects.get(question_id = question_id)

    active_rating = False

    if request.user.is_authenticated: #if user logged in increase the views by 1

        # Start Calculate intersting Questions
        # World,Sport,Business,Science
        user_interests = models.users.objects.get(username = request.user.username)
        user_interests_values = str(user_interests.interests).split(',')

        category_name = models.category.objects.get(question = question_id).categoryname
        category_list = ['World', 'Sport', 'Business', 'Science']

        count = 0
        for category in category_list:
            if category_name == category:
                if int(user_interests_values[count]) < 3:
                    user_interests_values[count] =  int(user_interests_values[count]) + 1

                    new_interested_values = ""
                    for interestValue in user_interests_values:
                        new_interested_values += str(interestValue) + ','

                    # Save New Interested Values
                    user_interests.interests = new_interested_values[:-1]
                    user_interests.save()
                    break

                elif int(user_interests_values[count]) == 3:
                    active_rating = True

            count += 1


        current_user_auth = request.user
        current_user = models.users.objects.get(username = current_user_auth.username)
        try:
            #if returned something that means the user visited this question before
            viewed_question = models.viewed_questions.objects.get(question = question_id, username = current_user_auth.username)
        except:
            viewed_question = models.viewed_questions()
            viewed_question.question = question
            viewed_question.username = current_user
            viewed_question.save()

            question.views += 1
            question.save()

    #notifications_details = models.notification.objects.get(event_number = question_id, event_title = 'q')
    all_answers = models.answer.objects.filter(question = question_id).order_by('-bestanswer')
    all_comments = []

    for i in all_answers:
        comment = models.comments.objects.filter(answer = i.answer_id)
        for j in comment:
            all_comments.append(j)


    # !!!!!!!!!
    all_category = models.category.objects.get(question = question_id)


    # Start get all image/images for current question
    first_question_image = models.imagesQuestion.objects.filter(question = question_id).first()
    question_images = models.imagesQuestion.objects.filter(question = question_id)[1:]
    question_images_count = models.imagesQuestion.objects.filter(question = question_id).count()


    # Start get likes of answers for speceific question
    liked_answers_list = []
    for answer in all_answers:
        try:
            models.liked_answers.objects.get(answer = answer.answer_id, username = request.user.username)
            liked_answers_list.append(True)
        except:
            liked_answers_list.append(False)


    # Get Numbers Of Followers
    try:
        user_followers = models.followers.objects.filter(followed_user = question.username.username).count()
    except:
        # if user deleted 
        user_followers = 0


    # Check if user make follow or not
    is_following = True
    try:
        followers = models.followers.objects.get(followed_user = question.username.username, follower = request.user)

    except:
        is_following = False


    # Start Visited Notification
    if request.user.is_authenticated:
        event_titles = ['q', 'a', 'm']

        for event in event_titles:
            try:
                visited_notification = models.notification.objects.filter(event_number = question_id, event_title = event, username = request.user.username)

                # if user has mentioned or make answer for the asme question
                for notification in visited_notification:
                    notification.seen = 1
                    notification.save()
                
            except:
                pass


    # Check if question is saved or not
    is_saved = True
    try:
        saved = models.saved_question.objects.get(saved_question = question_id, username = request.user.username)

    except:
        is_saved = False

    
    # Get Mentioned user
    mentioned_users = []
    all_mentioned_users = []
    all_mentioned_users_info = []

    for answer in all_answers:
        splited_mention = str(answer.content).split('<a href="/domanda/userprofile/')
        
        if len(splited_mention) == 1: # didn't split
            all_mentioned_users_info.append([])
            continue

        mentioned_users.append(splited_mention)

        for splited_content in mentioned_users:
            for z in splited_content[1:]:
                x = str(z).split('/"')
                all_mentioned_users.append(x[0])
            mentioned_users.clear()

            for mentioned_user in all_mentioned_users:
                user_info = models.users.objects.get(username = mentioned_user)
                mentioned_users.append(user_info)

            all_mentioned_users_info.append(mentioned_users[:])
            all_mentioned_users.clear()
            mentioned_users.clear()
    
    all_mentioned_users_following = []
    '''for mentionedUser in all_mentioned_users_info:
        temp_list = []
        for mentionedUserFollowing in mentionedUser:
            try:
                mentioned_following_user = models.followers.objects.get(followed_user = mentionedUserFollowing.username , follower = request.user)
                temp_list.append(True)
            except:
                temp_list.append(False)
        all_mentioned_users_following.append(temp_list)'''
            

    #zip(all_mentioned_users_info, all_mentioned_users_following)
    final_list = list(zip(all_answers, liked_answers_list))

    context = {
        'body':'body-background-img-color',
        'title': question.title,
        'question':question,
        'categories' : all_category,
        'allComments' : all_comments,
        'answers': final_list,
        'allAnswers': all_answers,
        'num_of_followers': user_followers,
        'isFollowing': is_following,
        'isSaved': is_saved,
        'active_rating': active_rating,
        'firstQuestionImage': first_question_image,
        'questionImages': question_images,
        'questionimagescount': question_images_count,
    }

    return render(request, 'get_question.html', context)


'''
******************************
****** Start Signin **********
******************************
'''

def signin(request):
    username = ''
    password = ''
    is_checked = True

    if "username" in request.COOKIES and "password" in request.COOKIES:
        username = request.COOKIES['username']
        password = request.COOKIES['password']

    if not username and not password:
        is_checked = False
        context = {
            'body':'body-background',
            'title':'Signin',
            'current_username' : username,
            'current_pass': password,
            'is_checked': is_checked
        }

    else:

        context = {
            'body':'body-background',
            'title':'Signin',
            'current_username' : username,
            'current_pass': password,
            'is_checked': is_checked
        }

    return render(request, 'signin.html', context)

def signin_process(request):
    if request.method == 'POST':
        Username = request.POST['signin-username']
        Password = request.POST['signin-pass']
        try:
            Remember_me = request.POST['signin-rememberme']
        except:
            Remember_me = 0


        data = {}  #'is_taken'

        user = User.objects.filter(username = Username)

        if not user:
            data['error_message'] = 'Incorrect Username'
            return JsonResponse(data)

        else:
            matchpass = check_password(Password, user[0].password)

            if matchpass == False:
                data['error_message'] = 'Incorrect Password'
                return JsonResponse(data)

            else: #success login
                result = authenticate(username = Username, password = Password)
                login(request, result)

                # Check if user verified his/her account or not
                verified_user = models.users.objects.get(username = Username)
                data['verified_or_not'] = verified_user.verified

                if Remember_me:
                    response = JsonResponse(data)
                    response.set_cookie('username', request.POST['signin-username'])
                    response.set_cookie('password', request.POST['signin-pass'])
                else:
                    response = JsonResponse(data)
                    response.delete_cookie('username')
                    response.delete_cookie('password')

                

                return response


'''
******************************
***** Start logout page *****
******************************
'''

def logout_process(request):
    logout(request)
    return HttpResponseRedirect('/domanda/signin')

'''
******************************
***** Start Sign Up page *****
******************************
'''

def signup(request):
    return render(request, 'signup.html', {'body':'body-background', 'title':'Signup'})

def signup_process(request):
    if request.method == 'POST':
        # Bring Input Data
        Username = request.POST['signup-username']
        Email = request.POST['signup-email']
        Password = request.POST['signup-pass']

        # Start Get Verification Code
        verify_code = random_code()

        try:
            # Add user to User Authentication Table
            user_auth = User.objects.create_user(Username, Email, Password)

        except:
            return HttpResponseRedirect('/domanda/signup')

        # Add User in Users of our app Table
        newUser = models.users()
        newUser.username = Username
        newUser.email = Email
        newUser.password = Password
        newUser.firstName = ''
        newUser.lastName = ''
        newUser.notifiy_count = 0
        newUser.profile_image = "profileImage/" + Username + '-' + Username[0].upper() + ".png"  # profileimage/khaled-K.png
        newUser.verify_code = verify_code

        user_auth.save()
        newUser.ua = user_auth
        newUser.save()

        x = "profileImage/Letters/" + Username[0].upper() + ".png"       # letters/K.png

        shutil.copy(x, 'profileImage/')
        os.rename("profileImage/" + Username[0].upper() + ".png", "profileImage/" + Username + '-' + Username[0].upper() + ".png")


        # Start Send Confirmation Mail
        subject = 'Welcome to Domanda .'
        message = 'Welcome ' + Username + ', \n\nYour account has been created successfully. \nYour verification code is ' + verify_code + '\n\nThis email was sent to ' + Email + ' as a member of Domanda.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [Email]

        send_mail(subject, message, from_email, to_list, fail_silently = False)

        return signin(request)

    else:
        return HttpResponseRedirect('/domanda/signup')

def signup_verification(request):
    context = {
        'body':'body-background',
        'title':'Signup Verification', 
    }
    return render(request, 'signup_verification.html', context)

def verify_account(request):
    data = {}

    if request.method == "POST":
        verify_code = request.POST['signup_verification_code']
        current_user = models.users.objects.get(username = request.user.username)

        if current_user.verify_code == verify_code:
            current_user.verified = 1
            current_user.save()
            data['verify_account'] = 'verified'

        else:
            data['verify_account'] = 'notVerified'

    return JsonResponse(data)

'''
******************************
***** Personal Profile *******
******************************
'''

def profile(request):
    user_Id = request.user.username

    current_user = models.users.objects.get(username = user_Id)
    form = forms.uploadProfileImage(request.POST, request.FILES, instance = current_user)

    # Start Get Posted Questions
    posted_question = models.questions.objects.filter(username = user_Id)
    all_category = models.category.objects.all()

    # Start Get Saved Questions
    saved_questions = models.saved_question.objects.filter(username = user_Id).order_by('-saved_question')

    # Start Get Followers For Current User
    followed_information = []
    all_followed_info = models.followers.objects.filter(followed_user = user_Id)

    for followed in all_followed_info:
        followed_info = models.users.objects.get(username = followed.follower)
        followed_information.append(followed_info)

    
    # Start Get Following Users
    following_information = []
    all_following_info = models.followers.objects.filter(follower = user_Id)

    for following in all_following_info:
        following_info = models.users.objects.get(username = following.followed_user.username)
        following_information.append(following_info)


    # Start Get Rating Values
    rating_values = str(current_user.interests).split(',')

    world = int(rating_values[0])
    sport = int(rating_values[1])
    business = int(rating_values[2])
    science = int(rating_values[3])

    if world <= 3:
        world = 0
    else:
        world -= 3

    if sport <= 3:
        sport = 0
    else:
        sport -= 3

    if business <= 3:
        business = 0
    else:
        business -= 3


    if science <=3:
        science = 0
    else:
        science -= 3

    context = {
        'body':'body-background-img-color',
        'title': user_Id ,
        'user_info': current_user,
        'posted_question': posted_question,
        'saved_questions': saved_questions,
        'followers': followed_information,
        'following': following_information,
        'categories' : all_category,
        'form' : form,
        'worldRating': world,
        'sportRating': sport,
        'businessRating': business,
        'scienceRating': science,
    }

    return render(request, 'personal_profile.html', context)


def profile_save(request):
    if request.method == "POST":
        userName = request.POST['profile-username']
        fullName = request.POST['profile-fullname']
        email    = request.POST['profile-email']
        country  = request.POST['profile-location']
        aboutme  = request.POST['profile-aboutme']
        websitLink = request.POST['profile-websitelink']
        twitterLink = request.POST['profile-twitterlink']
        githubLink  = request.POST['profile-github']
        workorschool = request.POST['profile-career']
        careerType   = request.POST['profile-career-type']
        careerValue  = request.POST['profile-career-value']
        worldRatingVal = request.POST['world_rating']
        sportRatingVal = request.POST['sport_rating']
        businessRatingVal = request.POST['business_rating']
        scienceRatingVal = request.POST['science_rating']


        if int(worldRatingVal) > 0: 
            worldRatingVal = int(worldRatingVal) + 3
        
        if int(sportRatingVal) > 0:
            sportRatingVal = int(sportRatingVal) + 3

        if int(businessRatingVal) > 0:
            businessRatingVal = int(businessRatingVal) + 3

        if int(scienceRatingVal) > 0:
            scienceRatingVal = int(scienceRatingVal) + 3

        ratingValues = str(worldRatingVal) + ',' + str(sportRatingVal) + ',' + str(businessRatingVal) + ',' + str(scienceRatingVal)

        lastName = ""

        # Split
        firstandlastname = fullName.split(' ')

        for i in firstandlastname[1:]:
            lastName += i + ' '


        editProfile = models.users.objects.get(username = userName);
        editProfile_auth = User.objects.get(username = userName)

        form = forms.uploadProfileImage(request.POST, request.FILES, instance = editProfile)

        oldImage = editProfile.profile_image;

        if form.is_valid():
            editProfile_auth.username = userName
            editProfile_auth.first_name = firstandlastname[0]
            editProfile_auth.last_name = lastName
            editProfile_auth.email = email

            editProfile.username = userName
            editProfile.firstName = firstandlastname[0]
            editProfile.lastName = lastName
            editProfile.email = email
            editProfile.country = country
            editProfile.aboutme = aboutme
            editProfile.WebsiteLink = websitLink
            editProfile.TwitterLink = twitterLink
            editProfile.GitHubLink = githubLink
            editProfile.workORschool = workorschool
            editProfile.career_type = careerType
            editProfile.career_value = careerValue
            editProfile.interests = ratingValues
            editProfile.ua = editProfile_auth

            x = str(oldImage).split('/')

            if oldImage != editProfile.profile_image:
                os.remove(str(oldImage))
                form.save()
            

            newImage = str(editProfile.profile_image).split('/')
            imageName = newImage[1].split('-')

            if imageName[0] != userName:
                os.rename(str(editProfile.profile_image), x[0] + '/' + userName + '-' + newImage[1])
                editProfile.profile_image = x[0] + '/' + userName  + '-' + newImage[1]

            editProfile.save()

        #------------------------------------
        rewardingAchievements(userName, 2)
        #------------------------------------

    return HttpResponseRedirect('/domanda/personalprofile/')
        

def profile_delete(request, user_id):
    oldUser = models.users.objects.get(username = user_id)
    oldUser_auth = User.objects.get(username = user_id)

    # Delete User Image
    os.remove(str(oldUser.profile_image))

    # Delete User From Following Table
    followed_users = models.followers.objects.filter(follower = user_id)

    for followed in followed_users:
        followed.delete()
    

    logout(request)

    oldUser.delete()
    oldUser_auth.delete()

    return HttpResponseRedirect('/domanda/signin')

'''
******************************
***** Users Profile **********
******************************
'''

def user_profile(request, user_Id):
    visited_user = models.users.objects.get(username = user_Id)
    form = forms.uploadProfileImage(request.POST, request.FILES, instance = visited_user)
    
    is_following = True

    try:
        followers = models.followers.objects.get(followed_user = user_Id, follower = request.user)

    except:
        is_following = False


    # Check if user_profile is visited or not
    if request.user.is_authenticated:
        try:
            visited_follower_notification = models.notification.objects.get(notification_content = user_Id , event_title = 'f', username = request.user.username)
            visited_follower_notification.seen = 1
            visited_follower_notification.save()

        except:
            pass


    # Return all Achievements for visited user
    all_Achievement = models.achievements.objects.filter(username = user_Id)

    context = {
        'body':'body-background-img-color',
        'title':'User Profile',
        'user_info': visited_user,
        'form' : form,
        'isFollowing': is_following,
        'userAchievements': all_Achievement,
    }

    return render(request, 'users_profile.html', context)

# Start Forget Password
def forgot_password(request):
    data = {}
    username = request.POST['username']

    try:
        #User app table
        user = models.users.objects.get(username = username)

        subject, from_email, to = 'Forgot Password', settings.EMAIL_HOST_USER , [user.email]
        html_content = '<img src="images/domanda_banner-01.png" />Here is your password <strong>' + user.username + ', <strong/> its ' + user.password + '<br/> we recomend changing your password for better security.'
        msg = EmailMultiAlternatives(subject, '', from_email, to)
        msg.attach_alternative(html_content, "text/html")
        #msg.attach_file('/images/domanda_banner-01.png')
        msg.send()

    except:
        data['message'] = 'username is not valid'
        return JsonResponse(data)

    data['message'] = 'An email with password has been sent to your email!'

    return JsonResponse(data)


#Start Achievements page
def achievement(request):
    if request.user.is_authenticated:
        ListOfAchievements = models.achievements.objects.filter(username = request.user.username)

        achievements = ['First Question!', '5th Question!', '10th Question!', '25th Question!', 
                        '50th Question!', '100th Question!', 'First Answer!', '5th Answer!', 
                        '10th Answer!', '25th Answer!', '50th Answer!', '100th Answer!', 
                        'First Best Answer!', '5th Best Answer!', '10th Best Answer!', '25th Best Answer!', 
                        '50th Best Answer!', '100th Best Answer!', 'Profile Completed!']
        
        booleanListOfAchievements = []

        for achievement in achievements:
            if not searchAchievements(achievement, ListOfAchievements):
                booleanListOfAchievements.append(True)
            else:
                booleanListOfAchievements.append(False)

        finalList = list(zip(achievements, booleanListOfAchievements))

        # Reset Achievemenst
        current_user = models.users.objects.get(username = request.user.username)
        current_user.achievement_count = 0
        current_user.save()
    
    context = {
        'body':'body-background-img-color',
        'title':'Achievements',
        'listOfAchievements': finalList,
    }

    return render(request, 'achievements.html', context)


#Start Notification page
def notification(request, user_id):
    all_notifications = models.notification.objects.filter(username = user_id).order_by('-date', '-time')
    user = models.users.objects.get(username = user_id)


    # Make Notoifcation Count Zero If user Visite Notification Page
    user.notifiy_count = 0
    user.save()

    if all_notifications is not None:

        notifiy_question_list = []
        notifiy_answer_list = []
        notifiy_followers_list = []
        notifiy_mentions_list = []
        

        for notifiy in all_notifications:
            if notifiy.event_title == 'q' or notifiy.event_title == 'u':
                notifiy_question_list.append(notifiy)

            elif notifiy.event_title == 'a':
                notifiy_answer_list.append(notifiy)

            elif notifiy.event_title == 'f':
                notifiy_followers_list.append(notifiy)

            elif notifiy.event_title == 'm':
                notifiy_mentions_list.append(notifiy)
        
        context = {
            'body':'body-background-img-color', 
            'title':'Notifications', 
            'notifications': all_notifications,
            'N_q_list': notifiy_question_list,
            'N_a_list': notifiy_answer_list,
            'N_f_list': notifiy_followers_list,
            'N_m_list': notifiy_mentions_list,
        }

    else:
        context = {
            'body':'body-background-img-color', 
            'title':'Notifications',
        }


        print(str(notifiy_mentions_list))

    return render(request, 'notifications.html', context)


# Start Load Next Questions
def loadNext(request, index):
    displayed_questions = request.session.get('displayed_questions')
    questions_list = []
    questions_list_id = []
    number_of_questions = models.questions.objects.all().count()
    questions = models.questions.objects.all()
    for i in questions:
        questions_list_id.append(i.question_id)
    i = 0
    while True:
        if questions_list_id[i] == index:
            i += 1
            break
        else:
            i += 1
    count = 0
    while count < 8:
        try:
            questions_list.append(models.questions.objects.get(question_id = questions_list_id[i]))
            displayed_questions += 1
        except:
            break
        i += 1
        count += 1
        
    request.session['displayed_questions'] = displayed_questions

    all_category = models.category.objects.all()

    context = {
        'body':'body-background-img-color',
        'title':'Home',
        'questions':questions_list,
        'lastquestion':questions_list[-1],
        'number_of_questions':number_of_questions,
        'displayed_questions':displayed_questions,
        'categories' : all_category,
    }
    
    return render(request, 'home.html', context)


# Start Load Previous Questions
def loadPrev(request, index):
    displayed_questions = request.session.get('displayed_questions')
    questions_list = []
    questions_list_id = []
    number_of_questions = models.questions.objects.all().count()
    questions = models.questions.objects.all()

    for i in questions:
        questions_list_id.append(i.question_id)
    i = 0
    while True:
        if questions_list_id[i] == index:
            i += 1
            break
        i += 1
    count = 8
    while count < i:
        count *= 2
    count //= 2
    diff = i - count
    i -= diff
    lastindex = i
    i -= 7
    displayed_questions -= diff
    while i <= lastindex:
        question = models.questions.objects.get(question_id = questions_list_id[i - 1])
        questions_list.append(question)
        i += 1
    request.session['displayed_questions'] = displayed_questions
    
    all_category = models.category.objects.all()

    context = {
        'body':'body-background-img-color',
        'title':'Home',
        'questions':questions_list,
        'lastquestion':questions_list[-1],
        'number_of_questions':number_of_questions,
        'displayed_questions':displayed_questions ,
        'categories' : all_category,
    }

    return render(request, 'home.html', context)


# Start Post Answer
def post_answer(request, user_id, question_id): 
    if request.method == "POST":

        #------------------------------------------------------------------#
        question = models.questions.objects.get(question_id = question_id)

        try:
            if question.username.username != user_id:
                user = models.users.objects.get(username = question.username.username)
            
            oldNotifiyCount = user.notifiy_count
            oldNotifiyCount += 1

            user.notifiy_count = oldNotifiyCount
            user.save()

            notifyuser = models.notification()

            notifyuser.notification_content = str(user_id)
            notifyuser.event_title = 'a'
            notifyuser.event_number = question_id
            notifyuser.username = user

            notifyuser.save()

        except:
            pass
            
        #-----------------------------------------------------------------#

        answer_content = request.POST['answer-content']
        data = {}

        answer = models.answer()

        answerd_user = models.users.objects.get(username = user_id)
        answerd_question = models.questions.objects.get(question_id = question_id)

        answerd_question.num_answers += 1

        # Get Mention User
        split_answerContent = str(answer_content).split('@')
        mention_user = []
        
        for i in split_answerContent[1:]:
            split_list_answerContent = i.split()
            mention_user.append(split_list_answerContent[0])


        # Get Last Record From Answers Table
        try:
            last_answer = models.answer.objects.all().last()
            new_answerID = last_answer.answer_id + 1
        except:
            new_answerID = 1

        for j in mention_user:
            mention_userProfile = '/domanda/userprofile/' + j + '/'
            mention_anchor = '<a href="' + mention_userProfile + '" data-userID = "' + str(new_answerID) + '-' + j + '">' + j + '</a>'
            mention_with_a = '@' + j
            answer_content = answer_content.replace(mention_with_a, mention_anchor)

            # Start Send Notification For Every Mentioned user
            mention_notifiy = models.notification()
            mentioned_user = models.users.objects.get(username = j)

            mention_notifiy.notification_content = user_id
            mention_notifiy.event_title = 'm'
            mention_notifiy.event_number = question_id
            mention_notifiy.username = mentioned_user

            mentioned_user.notifiy_count += 1

            mention_notifiy.save()
            mentioned_user.save()

       
        answer.content = answer_content
        answer.username = answerd_user
        answer.question = answerd_question

        
        answerd_question.save()
        answer.save()

        data['new_answer'] = answer.content
        data['mention-user'] = mention_user

        #------------------------------------
        rewardingAchievements(user_id, 1)
        #------------------------------------

    return JsonResponse(data)


# Start Check Best Answer
def best_answer(request, answer_id):
    data = {}

    '''if request.method == "POST":
        #answer_id = request.POST['answer_id']
        #best_answer_value = request.POST['best_answer']

        # Get Current Answer
        current_answer = models.answer.objects.get(answer_id = answer_id)

        current_answer.bestanswer = best_answer_value
        current_answer.save()

        print("Answer ID : " + str(answer_id))

        #------------------------------------
        user_id = current_answer.username.username
        rewardingAchievements(user_id, 3)
        #------------------------------------'''

    try:
        # Get Current Answer
        current_answer = models.answer.objects.get(answer_id = answer_id)
        old_bestAnswer = models.answer.objects.get(question = current_answer.question.question_id, bestanswer = 1)

        current_answer.bestanswer = 1
        old_bestAnswer.bestanswer = 0

        current_answer.save()
        old_bestAnswer.save()

    except:
        # Get Current Answer
        current_answer = models.answer.objects.get(answer_id = answer_id)

        current_answer.bestanswer = 1
        current_answer.save()


    #------------------------------------
    user_id = current_answer.username.username
    rewardingAchievements(user_id, 3)
    #------------------------------------

    return JsonResponse(data)


# Start Post Comment
def post_comment(request, user_id):
    data = {}

    if request.method == "POST":

        comments = models.comments()
        answered_user = models.users.objects.get(username = user_id)

        comment_content = request.POST['add_comment']
        comment_answerID = request.POST['answer_id']

        answer = models.answer.objects.get(answer_id = comment_answerID)

        comments.answer = answer
        comments.comment_content = comment_content
        comments.comment_user = answered_user

        comments.save()

        data['added-comment'] = comments.comment_content
        data['answer-id'] = comment_answerID

    return JsonResponse(data)


# Start Following users
def follow_user(request, user_followed, follower):
    user = models.users.objects.get(username = user_followed)
    user_follower = User.objects.get(username = follower)

    oldNotifiyCount = user.notifiy_count
    oldNotifiyCount += 1

    user.notifiy_count = oldNotifiyCount
    
    oldNumberFollowers = user.number_followers
    oldNumberFollowers += 1

    user.number_followers = oldNumberFollowers

    user.save()

    followed = models.followers()
    followed.followed_user = user
    followed.follower = follower
    followed.save()

    newNotification = models.notification()
    newNotification.notification_content = str(follower)
    newNotification.event_title = 'f'
    newNotification.event_number = user_follower.id
    newNotification.username = user
    newNotification.save()

    return home(request)


# Start Unfollowing User
def unfollow_user(request, user_followed, follower):
    followers = models.followers.objects.get(followed_user = user_followed, follower = follower)
    followers.delete()

    user = models.users.objects.get(username = user_followed)

    oldNumberFollowers = user.number_followers
    oldNumberFollowers -= 1

    user.number_followers = oldNumberFollowers

    user.save()

    return home(request)


# Start Search
def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''
    
    if request.POST['searchBy_value'] == 'Questions':
        search_result = models.questions.objects.filter(title__contains = search_text.lower())

    elif request.POST['searchBy_value'] == 'Users':
        search_result = models.users.objects.filter(username__contains = search_text.lower())
        
    return render_to_response('search_result.html', {'SearchResult' : search_result})


# Start Search by event (Enter)
def search_titles_eventEnter(request):

    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''

    
    if request.POST['searchBy_value'] == 'Questions':
        questions = models.questions.objects.filter(title__contains = search_text)

    elif request.POST['searchBy_value'] == 'Users':
        all_users = models.users.objects.filter(username__contains = search_text)
        following_list = []

        for allUsers in all_users:
            try:
                is_following = models.followers.objects.get(followed_user = allUsers.username, follower = request.user.username)
                following_list.append(True)
            except:
                following_list.append(False)

        final_list = list(zip(all_users, following_list))

        context = {
            'body':'body-background-img-color',
            'title':'All Profiles',
            'allUsers' : final_list,
        }
        return render(request, 'all_profiles.html', context)


    all_category = models.category.objects.all()

    context = {
        'body':'body-background-img-color',
        'title':'Home',
        'questions' : questions,
        'categories' : all_category,
    }

    return render(request ,'search_questions.html', context)


# Start Turn off Answers
def turn_off_on_answers(request, question_id):
    current_question = models.questions.objects.get(question_id = question_id)

    if current_question.turnoffcomment == 1:
        current_question.turnoffcomment = 0
    
    else:
        current_question.turnoffcomment = 1

    current_question.save()

    return HttpResponseRedirect('/domanda/question/' + str(current_question.question_id))


# Start Make Voting
def vote_question(request, question_id, vote_up):
    data = {}

    if request.user.is_authenticated:
        user_auth = request.user

        try:
            vote = models.voted_questions.objects.get(question = question_id, username = user_auth.username)
            question = models.questions.objects.get(question_id = question_id)
            if vote_up == 1:
                if vote.vote_up == False:
                    question.vote += 1
                    question.save()
                    vote.vote_up = True
                    vote.save()

                else:
                    data['voted_up'] = "You make voted up twice"
            else:
                if vote.vote_up:
                    question.vote -= 1
                    question.save()
                    vote.vote_up = False
                    vote.save()

                else:
                    data['voted_down'] = "You make voted down twice"
                
            data['voted'] = question.vote
            
        except:
            question = models.questions.objects.get(question_id = question_id)
            user = models.users.objects.get(username = user_auth.username)

            vote = models.voted_questions()
            vote.question = question
            vote.username = user

            if vote_up == 1:
                vote.vote_up = True
                question.vote += 1
                question.save()
            else:
                question.vote -= 1
                question.save()
            vote.save()

            data['voted'] = question.vote

    return JsonResponse(data)


# Start Likes 
def like_answer(request, answer_id):

    data = {}
    liked = True

    if request.user.is_authenticated:
        user_auth = request.user

        print('Answer id : ' + str(answer_id))

        try:
            liked_answer = models.liked_answers.objects.get(answer = answer_id, username = user_auth.username)
            liked_answer.delete()

            theAnswer = models.answer.objects.get(answer_id = answer_id)
            theAnswer.likes -= 1
            theAnswer.save()

            liked = False
            data['num_likes'] = theAnswer.likes
           
        except:
            theAnswer = models.answer.objects.get(answer_id = answer_id)
            user = models.users.objects.get(username = user_auth.username)
            liked_answer = models.liked_answers()

            print('The answer id : ' + str(theAnswer))

            liked_answer.answer = theAnswer
            liked_answer.username = user
            liked_answer.save()

            theAnswer.likes += 1
            theAnswer.save()

            data['num_likes'] = theAnswer.likes

        
    data['liked'] = liked

    return JsonResponse(data)


# Start Delete Question
def delete_question(request, questionID):
    question = models.questions.objects.get(question_id = questionID)
    question.delete()

    return HttpResponseRedirect('/')


# Start Save Selected Theme of Authenticated User
def save_theme(request, userid):
    data = {}

    auth_user = models.users.objects.get(username = userid)
    new_theme = request.POST['newTheme']

    auth_user.theme_path = new_theme
    auth_user.save()

    return JsonResponse(data)


# Start Filter Questions By Category
def get_questions_by_category(request, category_name):
    all_questions_category = models.category.objects.filter(categoryname = category_name)
    questions_list = []

    for category in all_questions_category:
        question = models.questions.objects.get(question_id = category.question.question_id)
        questions_list.append(question)

    questions_list.reverse()

    all_category = models.category.objects.all()

    return render(request, 'home.html', {'body':'body-background-img-color', 'title':'Home', 'questions':questions_list, 'categories' : all_category })


# Start Saved Question
def saved_question(request, question_id):

    data = {}
    is_saved = False

    user_name = request.user

    current_user = models.users.objects.get(username = user_name.username)
    question = models.questions.objects.get(question_id = question_id)

    try:
        saved = models.saved_question.objects.get(saved_question = question.question_id, username = current_user.username)
        saved.delete()

    except:
        saved_q = models.saved_question()

        saved_q.saved_question = question
        saved_q.username = current_user

        saved_q.save()

        is_saved = True

    data['saved'] = is_saved

    return JsonResponse(data)


# Start Search by month or week
def weekly_monthly_questions(request, weekly):
    today_date = datetime.date.today()
    if weekly == True:
        last_date = today_date - timedelta(days = 7)
    else:
        last_date = today_date - timedelta(days = 30)

    all_questions = models.questions.objects.all().order_by('-question_id')
    questions_list = []

    for question in all_questions:
        if question.date >= last_date and question.date <= today_date:
            questions_list.append(question)


    all_category = models.category.objects.all()

    context = {
        'body':'body-background-img-color',
        'title':'Home',
        'questions':questions_list,
        'categories' : all_category,
    }

    return render(request, 'home.html', context)


# Start Add New Rating Value
def add_rating(request):
    current_user = models.users.objects.get(username = request.user.username)
    old_rating_values = str(current_user.interests).split(',')

    # Get currebt category and new rating values
    current_category = request.POST['category_rating']
    new_rating_value = request.POST['rating_value']

    category_list = ['World', 'Sport', 'Business', 'Science']


    count = 0
    for category in category_list:
        if current_category == category:
            old_rating_values[count] = int(old_rating_values[count]) + int(new_rating_value)
            
            new_rating = ""
            for newRating in old_rating_values:
                new_rating += str(newRating) + ','

            current_user.interests = new_rating[:-1]
            current_user.save()
            break

        count += 1

    return JsonResponse({})


# Start Filter Questions By User Interesting
def interesting_questions(request):
    current_user = models.users.objects.get(username = request.user.username)
    current_rating_values = str(current_user.interests).split(',')

    category_list = ['World', 'Sport', 'Business', 'Science']
    edit_rating_values = []
    all_interesting_questions = []

    # Make subtraction operation (old_rate - 3)
    for newRatingValues in current_rating_values:
        if int(newRatingValues) > 3:
            newRate = (int(newRatingValues) - 3) * 10
            edit_rating_values.append(newRate)

        else:
            edit_rating_values.append(0) 
    

    temp_count = 0
    for category in category_list:
        objects_count = models.category.objects.filter(categoryname = category).count()
        number_of_questions = edit_rating_values[temp_count] * objects_count / 100

        all_category_objects = models.category.objects.filter(categoryname = category)
        
        num_q = 0
        while num_q < number_of_questions:
            all_interesting_questions.append(models.questions.objects.get(question_id = all_category_objects[num_q].question_id))
            num_q += 1

        temp_count += 1

    all_category = models.category.objects.all()

    shuffle(all_interesting_questions)

    context = {
        'body':'body-background-img-color',
        'title':'Home',
        'questions': all_interesting_questions,
        'categories': all_category,
    }

    return render(request, 'home.html', context)


# Start Change site mode
def change_mode(request):
    data = {}
    current_user = models.users.objects.get(username = request.user.username)
    
    try:
        site_mode = request.POST['change_site_mode']
    except:
        site_mode = 'off'


    if site_mode == 'on':
        current_user.mode_path = "light"

    else:
        current_user.mode_path = "dark"

    
    current_user.save()

    return JsonResponse(data)


# Start Trending Question
def Trending_questions(request):

    today_date =  datetime.date.today()
    trending_questions = models.questions.objects.filter(date = today_date)
    trending_questions_list = []

    for trendingQuestion in trending_questions:
        trending_questions_list.append(trendingQuestion)

    trending_questions_list.sort(key = lambda question: question.vote + question.views + question.num_answers, reverse = True)


    all_category = models.category.objects.all()

    context = {
        'body':'body-background-img-color',
        'title':'Home',
        'questions':trending_questions_list,
        'categories' : all_category,
    }

    return render(request, 'home.html', context)


# Start Edit Question
def edit_question(request, questionId):
    data =  {}

    new_question_title = request.POST['question-edit-title']
    new_question_content = request.POST['question-edit-body']

    current_question = models.questions.objects.get(question_id = questionId)
    current_question.title = new_question_title
    current_question.content = new_question_content

    current_question.save()

    return JsonResponse(data)