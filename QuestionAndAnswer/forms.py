from django import forms
from QuestionAndAnswer.models import users, imagesQuestion


class uploadProfileImage(forms.ModelForm):
    class Meta:
        model = users
        fields = ['profile_image']



class uploadQuestionImage(forms.ModelForm):
    class Meta:
        model = imagesQuestion
        fields = ['image']