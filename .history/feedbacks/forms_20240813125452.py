from students.models import FeedbackCategory, FeedbackQuestion, FeedbackOption ,FeedbackCategory
from django.forms import ModelForm
from students.models import Feedback 


class feedbackCategrory
class feedbackform(ModelForm):
    class Meta:
        model=Feedback
        fields=["teacher","feedback_text",]
        

class FeedbackQuestionForm(ModelForm):
    class Meta:
        model = FeedbackQuestion
        fields = ['category', 'question_text', 'question_type']

class FeedbackOptionForm(ModelForm):
    class Meta:
        model = FeedbackOption
        fields = ['option_text']
