from students.models import FeedbackCategory, FeedbackQuestion, FeedbackOption ,feedca
from django.forms import ModelForm
from students.models import Feedback 

class feedbackform(ModelForm):
    class Meta:
        model=Feedback
        fields=["teacher","feedback_text",]
        
from django import forms

class FeedbackQuestionForm(forms.ModelForm):
    class Meta:
        model = FeedbackQuestion
        fields = ['category', 'question_text', 'question_type']

class FeedbackOptionForm(forms.ModelForm):
    class Meta:
        model = FeedbackOption
        fields = ['option_text']
