/*global $, window, document*/
$(document).ready(function () {
    'use strict';

    /***********************
        Start Navbar
    ************************/
    $('[data-toggle="tooltip"]').tooltip();

    /************************************/
    /*Start Make Shortcuts in our system*/
    /************************************/
    /*
    s = search
    a = ask a question
    n = next
    p = previous
    j = next question
    k = previous question
    i = interesting
    t = trending
    w = week
    m = month
    c = categories(Tags)
    Enter = open a question
    */

    /*$(window).keyup(function (event){
        // (1) s = search
        /*if (event.keyCode == 83) {
            $('.domanda-navbar #domanda-content #form-search input[type="text"]').focus();
        }

        // (2) a = ask a question
        if (event.keyCode == 65) {
            $('.domanda-home-content .domanda-home-askQ');
        }

        // (3) n = next
        else if (event.keyCode == 78){
            $('.domanda-home-content .domanda-home-questionsControl .next_button').focus();
        }

        // (4) p = previous
        else if (event.keyCode == 80) {
            $('.domanda-home-content .domanda-home-questionsControl .previous_button').focus();
        }

        // (5) j = next question
        else if (event.keyCode == 74) {
            
        }

        // (6) k = previous question
        else if (event.keyCode == 75) {
            
        }

        // (7) i = interesting
        else if (event.keyCode == 73) {
            $('.domanda-home-importantQ ul li:first-of-type a').focus();
        }

        // (8) t = trending
        else if (event.keyCode == 84) {
            $('.domanda-home-importantQ ul li:nth-of-type(2) a').focus();
        }

        // (9) w = week
        else if (event.keyCode == 87) {
            $('.domanda-home-importantQ ul li:nth-of-type(3) a').focus();
        }

        // (10) m = month
        else if (event.keyCode == 77) {
            $('.domanda-home-importantQ ul li:nth-of-type(4) a').focus();
        }

        // (11) c = categories(Tags)
        /*else if (event.keyCode == 67) {
            $('.domanda-home-importantQ ul li:nth-of-type(5) a').focus();
        }
    });*/


    /************************************/
    /*End Make Shortcuts in our system*/
    /************************************/

    /*Display Links in fixed psoition when scroll to bottom*/
    var navbarHeight = $('.domanda-navbar').innerHeight();


    /*********************
    // Satrt Home and Body
    **********************/

    $('.domanda-signin-content .domanda-signin-form .domanda-signin-email form a').click(function (event) {
        event.preventDefault();

        var forgetPass_Form = $('.domanda-signin-content .domanda-signin-form .domanda-signin-email form'),
            forgetPass_username = $('.domanda-signin-content .domanda-signin-form .domanda-signin-email form input[type="text"]'),
            signin_username = $('.domanda-signin-content .domanda-signin-form .signinForm .signin_username');

        if (signin_username.val() == ""){
            $('.domanda-signin-form-alert-username').text('Username is required');
        }
        
        else{
            // Set forget password username with signin username input
            forgetPass_username.val(signin_username.val());

            $.ajax({
                type: forgetPass_Form.attr('method'),
                url: forgetPass_Form.attr('action'),
                data: forgetPass_Form.serialize(),
                dataType: 'json',

                success: function(data){
                    if (data['message']) {
                        signin_username.val('');
                        $('.domanda-display-message').fadeIn(400, function () {
                            $(this).delay(5000).fadeOut(400);
                        });
                        $('.domanda-display-message span').text(data['message']);
                    }
                }
            });
        }
    });

    // Start Hide Fcous in search
    $('.domanda-navbar .domanda-search input[type="text"]').focusin(function () {
        var placeholderValue = $(this).attr('placeholder');
        $(this).attr('placeholder', ' ');

        $(this).focusout(function () {
            $(this).attr('placeholder', placeholderValue);
        });
    });

    // Start Select Search By value
    $('.domanda-navbar .domanda-search select').change(function () {
        $('.domanda-navbar .domanda-search #searchby_id').val($(this).val());
    });

    // Start Choose Rating Value and save it in database
    $('.domanda-answers-rating-container .domanda-answers-rating .domanda-answers-rating-values span').click(function () {

        // Set new Rating Value to input
        $('.domanda-answers-rating-container .domanda-answers-rating .domanda-answers-rating-values form input[name="rating_value"]').val($(this).attr('data-ratingValue'));

        var rating_form = $('.domanda-answers-rating-container .domanda-answers-rating .domanda-answers-rating-values form');

        $.ajax({
            type: rating_form.attr('method'),
            url: rating_form.attr('action'),
            data: rating_form.serialize(),
            dataType: 'json',

            success: function () {
                $('.domanda-answers-rating-container').addClass('d-none');
            }
        });
    });

    // Start Change Mode of site
    $('.domanda-navbar .domanda-home-notify-userContent .domanda-switch-mode input[type="checkbox"]').change(function () {
        var siteMode_Form = $('.domanda-navbar .domanda-home-notify-userContent .domanda-switch-mode form');

        $.ajax({
            type: siteMode_Form.attr('method'),
            url: siteMode_Form.attr('action'),
            data: siteMode_Form.serialize(),
            dataType: 'json',

            success: function (data) {
                if($('.domanda-navbar .domanda-home-notify-userContent .domanda-switch-mode input[type="checkbox"]').prop('checked') == true) {
                    $("link[href *= 'mode").attr('href', '/static/QuestionAndAnswer/css/modes/light-mode.css');
                } else {
                    $("link[href *= 'mode").attr('href', '/static/QuestionAndAnswer/css/modes/dark-mode.css');
                }
            }
        });

    });

    // Start Change Site Theme
    $('.domanda-change-theme ul li').click(function () {
        var selected_theme = '/static/QuestionAndAnswer/css/themes/' + $(this).attr('data-theme-value'),
            theme_form = $('.domanda-change-theme form');

        $("link[href *= 'theme']").attr('href', selected_theme);

        $.ajax({
            type : "POST",
            url : theme_form.attr('action'),
            data : {
                'csrfmiddlewaretoken' : $('.domanda-change-theme form input[type="hidden"]').val(),
                'newTheme' : selected_theme
            },
            dataType : "json",
            success : function (data) {
                
            }
        });

    });

    // Start Chage site theme
    $('.domanda-change-theme div i').click(function () {
        $('.domanda-change-theme').toggleClass('active');
    });

    var navHeightinPx = navbarHeight + "px";
    $('body').css('padding-top', navHeightinPx);

    // Start Display Notification after post question
    $('.domanda-display-notification').each(function () {
        $(this).animate({
            left : 20 + 'px'
        }, 600, function () {
            $(this).delay(2000).animate({
                left : -370 + 'px'
            }, 1000);
        });

        $.playSound("static/QuestionAndAnswer/images/Notification_Sound_Effect_02.mp3");
    });

    // Start Display Category List
    $('.domanda-home-importantQ .category-list').click(function () {
        $('.domanda-home-importantQ .domanda-home-importantQ-category').toggleClass('d-none');
    });

    // Start Search on Eevent ( Keyup )
    $('#domanda-search').keyup(function (e) {
        $.ajax({
            type : "POST",
            url : '/domanda/search/',
            data : $('#form-search').serialize(),
            success : function (data, textStatus, jqXHR) {
                if ($('#domanda-search').val() != "") {
                    $('.domanda-search-result').removeClass('d-none');
                    $('.domanda-search-result').addClass('d-block');
                    $('.domanda-search-result').html(data);
                } else {
                    $('.domanda-search-result').removeClass('d-block');
                    $('.domanda-search-result').addClass('d-none');
                }
            },

            dataType : 'html'
        });
    });

    // Start Display Info For User That Post Question
    $('.domanda-answers-content .domanda-answers-questionContent span a:first-of-type').hoverDelay({
        delayIn: 100,
        delayOut:1200,
        handlerIn: function($element){
            var x = $('.domanda-answers-content .domanda-answers-questionContent span a:first-of-type span').position();
            $('.domanda-answers-content .domanda-answers-questionContent span .card.card_hover_link').css({
                'top': x.top - 217 + "px",
                'left': x.left + 15 + "px"
            });
        
            $('.domanda-answers-content .domanda-answers-questionContent span .card').removeClass('d-none');
        },

        handlerOut: function($element){
            
        }
    });

    $('.domanda-answers-content .domanda-answers-questionContent span .card').hoverDelay({
        delayIn: 100,
        delayOut:200,

        handlerIn: function($element){
            
        },

        handlerOut: function($element){
           $('.domanda-answers-content .domanda-answers-questionContent span .card').addClass('d-none');
        }
    });

    // Start Display Information For Mentioned User
    $('.domanda-answers-content .domanda-answers-add-newanswer .domanda-answers-answeredQuestions .domanda-answers-answerContent a').hoverDelay({
        delayIn: 200,
        delayOut:500,
        
        handlerIn: function($element){
            var mentioned_userid = $($element).attr('data-userid'),
                hash_for_id = '#';
            $('.domanda-answers-content .domanda-answers-add-newanswer .domanda-answers-answeredQuestions .card').css({
                'left': $element.position().left + 40 + 'px',
                'top': '-' + $('.domanda-answers-content .domanda-answers-add-newanswer .domanda-answers-answeredQuestions .card').innerHeight() + 'px'
            });
            $(hash_for_id.concat(mentioned_userid)).removeClass('d-none');
        },

        handlerOut: function($element){
            $('.domanda-answers-content .domanda-answers-add-newanswer .domanda-answers-answeredQuestions .card').addClass('d-none');
        }
    });

    
    /***********************
    ****Start Profile Page *
    ************************/

    /*Click to choice the career*/
    $('.domanda-profile-content .domanda-profile-career input[type="radio"]').click(function () {
        $(this).addClass('active-btn').siblings().removeClass('active-btn');
    });


    // Check if full name has number
    $('.domanda-profile-content form.domanda-profile-content-form').submit(function (e){

        var profile_fullname = $('.domanda-profile-content form.domanda-profile-content-form #fullname').val();

        //var isnum = /^\d+$/.test(profile_fullname);
        var hasNumber = /\d/;

        if(hasNumber.test(profile_fullname)){
            e.preventDefault();
            alert("Your fullname should be only letters");
        }
    });

    /*Change profile picture action*/
    function imagePreview(inputFile){
        if (inputFile.files && inputFile.files[0]) {
            var reader = new FileReader()

            reader.onload = function (e) {
                $('.domanda-profile-allContents .domanda-profile-content .domanda-profile-img').css({
                    'background': 'url(' + e.target.result + ')',
                    'background-repeat': 'no-repeat',
                    'background-position': 'center',
                    'background-size': 'cover'
                });
            }

            reader.readAsDataURL(inputFile.files[0]);

        }
    }

    /*This action if user select his new image*/
    $('.domanda-profile-img #id_profile_image').change(function () {

        if ($(this).val() != '') {
            imagePreview(this);
        }
    });

    // Start Display Input For Selected Category
    $('.domanda-profile-content .domanda-profile-rating').change(function () {
        if ($(this).val() == 'Choose_Category'){
            $('.domanda-profile-content .domanda-profile-rating-values input[type="number"]').attr('hidden', 'true');
        }

        var category_id = '#' + $(this).val();
        $(category_id).removeAttr('hidden').siblings().attr('hidden', 'false');
    });

    // Prevent user from make rating greater than 10
    $('.domanda-profile-content .domanda-profile-rating-values input[type="number"]').keypress(function (e) {
        if ($(this).val() > 10) {
            e.preventDefault();
            $(this).val(10);
        }

        else if ($(this).val() < 0){
            e.preventDefault();
            $(this).val(0);
        }
    });

    // Start Display Confirmation Message Before Delete The Account
    $('.domanda-profile-content .domanda-profile-actions a').click(function (e) {
        e.preventDefault();
        $('.domanda-deleteAccount-confirmation').show();
    });

    $('.domanda-deleteAccount-confirmation .domanda-deleteAccount-confirmation-controls button').click(function () {
        $('.domanda-deleteAccount-confirmation').hide();
    });

    /**************************
    ****Start Notification Page
    **************************/
    $('.domanda-Notification-heading ul li a').click(function () {
       $(this).addClass('active').siblings().removeClass('active');
    });


    // Start Select Type of display (all, questions, answers, followers)
    $('.domanda-Notification-displayType ul li').on('click', function () {
        $(this).addClass('active').siblings().removeClass('active');
        
        $('.domanda-allNotifications-type > section').hide();
        $($(this).attr('data-notifiy-displayType')).show();
    });


    // Start Select Option in User Profile
    $('.domanda-Notification-profile-displayType ul li').on('click', function () {
        $(this).addClass('active').siblings().removeClass('active');
        $('.domanda-profile-allContents > section').hide();
        $($(this).attr('data-profile-content')).show();
    });


    /***********************/
    //Start Signin Page
    /***********************/

    // AJAX for send data to signin view
    $('.domanda-signin-form .signinForm').submit(function (e) {
        e.preventDefault();

        var name = $('.domanda-signin-form .signin_username').val(),
            password = $('.domanda-signin-form .signin_pass').val();

        var myForm = $(this);

        if (name == "") {
            $('.domanda-signin-form-alert-username').text("Username is required");
            $('.domanda-signin-form-alert-pass').text('');
        } else if(password == "") {
            $('.domanda-signin-form-alert-pass').text("Password is required");
            $('.domanda-signin-form-alert-username').text('');
        } else {

            $.ajax({
                type: myForm.attr('method'),
                url: myForm.attr('action'),
                data: myForm.serialize(),
                dataType: 'json',
                success: function (data) {
                    /*If username is incorrec*/
                    if (data['error_message'] == "Incorrect Username") {
                        $('.domanda-signin-form-alert-username').text(data['error_message']);
                        $('.domanda-signin-form-alert-pass').text('');

                      /*If Password is incorrec*/
                    } else if(data['error_message'] == "Incorrect Password") {
                        $('.domanda-signin-form-alert-pass').text(data['error_message']);
                        $('.domanda-signin-form-alert-username').text('');

                      /*If username is valid and not verified account*/
                    } else if(data['verified_or_not'] == 0) {
                        window.location = '/domanda/signupverification';

                      /*If username is valid and verified account*/
                    } else {
                        window.location = '/';
                    }
                }
            });
        }
    });

    
    /***********************/
    //Start verify Page
    /***********************/
    $('.domanda-signup-verification form').submit(function (e){
        e.preventDefault();

        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            dataType: 'json',

            success: function(data){
                if(data['verify_account'] == "notVerified"){
                    $('.domanda-signup-verification .domanda-alert-verify').text('Your account has not verified');
                }

                else{
                    window.location = '/';
                }
            }

        });
    });


    /***********************/
    //Start Answers Page
    /***********************/

    // Start Post Answer
    $('.domanda-answers-content .domanda-answers-addComment #domanda-answer').submit(function (e) {
        e.preventDefault();

        var myform = $(this);

        $.ajax({
            type: "POST",
            url: myform.attr('action'),
            data: myform.serialize(),
            dataType: 'json',

            success : function (data) {
                $('.domanda-answers-add-newanswer').append('<div class="domanda-answers-answeredQuestions"> ' + data['new_answer']  +  '</div>');
                location.reload(true);
                $('.domanda-answers-content .domanda-answers-addComment #domanda-answer textarea').val('');
            }
        });
    });


    // Start Make Mention When User make Comment
    var x = false;
    $('.domanda-answers-content .domanda-answers-addComment #domanda-answer textarea').keyup(function () {
        var myValue = $(this).val(),
            lastchar = myValue[myValue.length - 1];
        
        if( lastchar == '@' ) {
            x = true;
        }

        if (x == true) {
            var mention_username = myValue.substring(myValue.lastIndexOf("@") + 1, myValue.length);
                
            if (mention_username != ''){
                $.ajax({
                    type : "GET",
                    url : '/domanda/alluser/' + mention_username,
                    dataType : "json",

                    success : function (data) {
                        var myListOfObjects =  [];

                        for(var i = 0; i < data['all_user'].length; i++){
                            myListOfObjects.push({username : data['all_user'][i]});
                        }

                        $('.domanda-answers-content .domanda-answers-addComment #domanda-answer textarea').suggest('@', {
                            data: myListOfObjects,
                            map: function(user) {
                              return {
                                    value: user.username,
                                    text: '<a>' + user.username + '</a>'
                                }
                            }
                        });
                    }       
                });

               
            }
        }
    });


    // Start Display Add Comment Input
    $('.domanda-answers-add-newanswer .domanda-answers-answeredQuestions .domanda-addComment-icon').click(function () {
        $('.domanda-answers-add-newanswer .domanda-answers-addComment-form').toggleClass('d-none');
    });


    // Start Display user information when make hover in mentioned users
    $('.domanda-answers-content .domanda-answers-add-newanswer .domanda-answers-answeredQuestions p a').hover(function () {
        
    });

    // Constaruct Hiddent Input With Answer ID
    $('.domanda-answers-add-newanswer .domanda-addComment-icon').on('click' ,function () {
        var answerID = $(this).attr('data-answerID');
        
        //var commentForm_id = $('.domanda-answers-add-newanswer .domanda-answers-addComment-form').attr('data-addComment-answerID');

        for(var i = 0; i < $('.domanda-answers-add-newanswer .domanda-answers-addComment-form').length; i++) {
            var x = $('.domanda-answers-add-newanswer .domanda-answers-addComment-form')[i];
            
            if ($(x).attr('data-addComment-answerID') !== answerID) {
                $(x).toggleClass('d-none');
            }
        }

        $('.domanda-answers-add-newanswer .domanda-answers-addComment-form input[type="hidden"]:last-of-type').val(answerID);
    });


    // Start Display Comments For Everey Selected Answer
    $('.domanda-answers-add-newanswer .domanda-displayComments-icon').on('click', function () {
        var answerID = $(this).attr('data-DanswerID');
        var commentID = 'com-' + answerID;

        for(var i = 0; i < $('.domanda-answers-userAnswered').length; i++) {
            var x = $('.domanda-answers-userAnswered')[i];
            
            if ($(x).attr('data-id') === commentID) {
                $(x).toggleClass('d-none');
            }
        }
    });


    // Start Send Comment to server
    $('.domanda-answers-add-newanswer #domanda-addComment').submit( function(e) {
        e.preventDefault();

        $.ajax({
            type : $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            dataType: 'json',

            success: function (data) {
                location.reload();
                $('.domanda-answers-add-newanswer .domanda-answers-addComment-form input[type="text"]').val('');
            }
        });
    });


    // Start make voting count up
    $('.domanda-answers-content .domanda-answers-questionContent .domanda-answers-questionContent-vote a:first-of-type').click(function (e) {
        e.preventDefault();
        var Current_voting_count = $('.domanda-answers-content .domanda-answers-questionContent .domanda-answers-questionContent-vote .domanda-answers-questionContent-voteNumber');

        var vote_form = $('.domanda-answers-content .domanda-answers-questionContent .domanda-answers-questionContent-vote form').serialize();

        $.ajax({
            type : "POST",
            url : $(this).attr('href'),
            data : vote_form,
            dataType : 'json',

            success : function (data) {
                if (data['voted_up']) {
                    // Start Display Custom Alert
                    $('.domanda-display-message').each(function () {
                        $('.domanda-display-message span').text(data['voted_up']);
                        $(this).animate({
                            transform : 'translateY(0px)'
                        }, 1000, function () {
                            $(this).delay(2000).animate({
                                transform : 'translateY(-30px)'
                            }, 1000);
                        });
                    });
                }

                else {
                    var vote_count = data['voted'];
                    $(Current_voting_count).text(vote_count);
                }
            }

        });
    });


    // Start make voting count down
    $('.domanda-answers-content .domanda-answers-questionContent .domanda-answers-questionContent-vote a:last-of-type').click(function (e) {
        e.preventDefault();
        var Current_voting_count = $('.domanda-answers-content .domanda-answers-questionContent .domanda-answers-questionContent-vote .domanda-answers-questionContent-voteNumber');
        
        var vote_form = $('.domanda-answers-content .domanda-answers-questionContent .domanda-answers-questionContent-vote form').serialize();

        $.ajax({
            type : "POST",
            url : $(this).attr('href'),
            data : vote_form,
            dataType : 'json',

            success : function (data) {
                if (data['voted_down']) {
                    // Start Display Custom Alert
                    $('.domanda-display-message').each(function () {
                        $('.domanda-display-message span').text(data['voted_down']);
                        $(this).animate({
                            transform : 'translateY(0px)'
                        }, 1000, function () {
                            $(this).delay(1300).animate({
                                transform : 'translateY(-30px)'
                            }, 1000);
                        });
                    });
                }

                else{
                    var vote_count = data['voted'];
                    $(Current_voting_count).text(vote_count);
                }
            }

        });
    });


    // Start make like for answers
    $('.domanda-answers-add-newanswer .domanda-makeLike-icon').click(function () {
        var myLikedForm = $('.domanda-answers-add-newanswer #liked_form').serialize(),
            answer_id = $(this).attr('data-answerID');

        $.ajax({
            type : "POST",
            url : '/domanda/likeanswer/' + parseInt(answer_id),
            data : myLikedForm,
            
            success : function (data) {
                if (data['liked'] == true) {
                    for(var i = 0; i < $('.domanda-answers-add-newanswer .domanda-makeLike-icon').length; i++) {
                        var current_answerid = $('.domanda-answers-add-newanswer .domanda-makeLike-icon')[i];

                        if (answer_id == $(current_answerid).attr('data-answerID')) {
                            $(current_answerid).css('color', '#D03939');
                            $(current_answerid).attr('title', data['num_likes']);
                            break;
                        }
                    }
                } 
                
                else {
                    for(var i = 0; i < $('.domanda-answers-add-newanswer .domanda-makeLike-icon').length; i++) {
                        var current_answerid = $('.domanda-answers-add-newanswer .domanda-makeLike-icon')[i];

                        if (answer_id == $(current_answerid).attr('data-answerID')) {
                            $(current_answerid).css('color', '#d0d0d0');
                            $(current_answerid).attr('title', data['num_likes']);
                            break;
                        }
                    }
                }
            }


        });
    });


    // Start Save Question
    $('.domanda-answers-content .domanda-answers-content-makeOperation #domanda-savequestion-form').submit(function (e) {
        e.preventDefault()

        var saved_question_form = $(this);

        $.ajax({
            type : 'POST',
            url : saved_question_form.attr('action'),
            data : saved_question_form.serialize(),
            dataType : 'json',

            success : function (data) {
                //alert(data['saved']);
            }

        });
    });


    // Start Display Question Image
    $('.domanda-answers-content .domanda-answers-questionContent .domanda-answers-questionContent-image').click(function () {
        $('.domanda-display-questionImage').css('transform', 'scale(1)');
    });
    
    $('.domanda-display-questionImage i').click(function () {
        $('.domanda-display-questionImage').css('transform', 'scale(0)')
    });


    $('.domanda-answers-content .domanda-answers-answeredQuestions .domanda-answers-bestanswer-form i.click-bestAnswer').click(function(e){
        e.preventDefault();
        
        var allForms = $('.domanda-answers-content .domanda-answers-answeredQuestions .domanda-answers-bestanswer-form');
        for(var x = 0; x < allForms.length; x++){
            if($(allForms[x]).find('i').css('color') == "rgb(26, 188, 156)"){
                $(allForms[x]).find('i').css('color', '#fff');
            }
        }

        $(this).css('color', '#1abc9c');

        $.ajax({
            type: "POST",
            url: $(this).parent('a').attr('href'),
            data: $(this).parent('a').parent('form.domanda-answers-bestanswer-form').serialize(),
            dataType: 'json',

            success: function (data){
                
            }
        });

        //console.log($(this).parent('a').parent('form.domanda-answers-bestanswer-form'));
    })

    // Start send question report to server
    $('.domanda-answers-content .domanda-answers-content-makeOperation a.reportQuestion').click(function (event) {
        event.preventDefault();
        $('.domanda-answers-makeReport').toggleClass('d-none');
    });

    $('.domanda-answers-makeReport .domanda-answers-makeReport-content .domanda-answers-makeReport-controls button').click(function () {
        $('.domanda-answers-makeReport').toggleClass('d-none');
    });

    $('.domanda-answers-makeReport .domanda-answers-makeReport-content .domanda-answers-makeReport-reportType').change(function (){
        if ($(this).val() == "answer"){
            $('.domanda-answers-makeReport .domanda-answers-makeReport-content .domanda-answers-makeReport-selectedAnswer').toggleClass('d-none');
        }

        else{
            $('.domanda-answers-makeReport .domanda-answers-makeReport-content .domanda-answers-makeReport-selectedAnswer').addClass('d-none');
        }
    });

    $('.domanda-answers-makeReport .domanda-answers-makeReport-content form').submit(function (event) {
        event.preventDefault();

        $('.domanda-answers-makeReport').toggleClass('d-none');
    });

    // Start Edit Question
    $('.domanda-answers-content .domanda-answers-content-makeOperation a.editQuestion').click(function (e){
        e.preventDefault();
        $('.domanda-answer-editQuestion').toggleClass('d-none');
    });

    $('.domanda-answer-editQuestion .domanda-answer-editQuestion-content .domanda-answer-editQuestion-controls button.domanda-answer-editQuestion-cancel').click(function () {
        $('.domanda-answer-editQuestion').toggleClass('d-none');
    });

    $('.domanda-answer-editQuestion .domanda-answer-editQuestion-content form').submit(function (e) {
        e.preventDefault();
        var question_title_value = $('.domanda-answer-editQuestion .domanda-answer-editQuestion-content #questionTitle'),
            question_content_value = $('.domanda-answer-editQuestion .domanda-answer-editQuestion-content #questionBody'),
            question_title_div = $('.domanda-answers-content .domanda-answers-question-title'),
            question_content_div = $('.domanda-answers-content .domanda-answers-question-content')

        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            dataType: 'json',

            success: function (data){
                question_title_div.text(question_title_value.val());
                question_content_div.text(question_content_value.val());
                $('.domanda-answer-editQuestion').toggleClass('d-none');
            }

        });
        
    });

});