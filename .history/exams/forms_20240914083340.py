from datetime import datetime, date
from students.models import Test ,Question,Option
from django import forms
from django.forms import ModelForm ,DateInput

class ExamsForm(ModelForm):
    # start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    # end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Test
        fields = ['title', 'subject', 'conducted_by','classgroup',
                  'test_date','start_time','end_time',]
        widgets = {
            'test_date':forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        test_date = cleaned_data.get('test_date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        classgroup = cleaned_data.get('classgroup')

        # Check if test date is in the future
        if test_date and test_date < date.today():
            self.add_error('test_date', 'Test date must be in the future.')

        # Required field validation
        if not title:
            self.add_error('title', 'Title is required.')
        if not start_time:
            self.add_error('start_time', 'Start time is required.')
        if not end_time :
            self.add_error('end_time', 'End time is required.')
        if not classgroup:
            self.add_error('classgroup', 'Class group is required.')
        if start_time > end_time:
            self.add_error
        # if end_time < start_time:
        #     self.add_error('end_time','end time should be gretter')
        return cleaned_data


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title is required.')
        # if 'exam' or 'test'  not in title.lower():
        #     raise forms.ValidationError('Title must contain the word "exam".')
        return title

    def clean_test_date(self):
        test_date = self.cleaned_data.get('test_date')
        if test_date:
            if isinstance(test_date, datetime):
                test_date = test_date.date() 
            if test_date < date.today():
                raise forms.ValidationError('Test date must be in the future.')
        return test_date  
     
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
class Question_text_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_text', 'is_correct']

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        if question:
            self.fields['option_text'].queryset = question.options.all()
        self.fields['is_correct'].widget = forms.CheckboxInput() 
        

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_text']

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['option_text'].queryset = question.options.all()
        self.fields['option_text'].widget = forms.RadioSelect()