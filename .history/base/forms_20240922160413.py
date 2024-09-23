from django.forms import ModelForm
from students.models import Student ,Teacher ,Subject  ,CustomUser ,hod
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'email', 'password1', 'password2', 'user_type')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['class'] = 'login__input'


    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # self.fields['user_type'].widget = forms.RadioSelect(choices=CustomUser.USER_TYPE_CHOICES)
    # super(room_form, self).__init__(*args, **kwargs)
    # for field_name, field in self.fields.items():
    #     field.widget.attrs['placeholder'] = field.label
    #     field.widget.attrs['class'] = 'login__input'

class subjectform(ModelForm):
    class Meta:
        model=Subject 
        fields=['name']     
    def __init__(self, *args, **kwargs):
        super(subjectform, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
class studuntform(ModelForm):
    class Meta:
        model=Student 
        fields=['roll_no','classgroup','profile']  
        
    def clean(self):
        cleaned_data = super().clean()
        classgroup=cleaned_data.get('classgroup')
        roll_no=cleaned_data.get('roll_no')
        if not classgroup:
             self.add_error('classgroup','classgroup should be selected ')
        if not roll_no:
             self.add_error('roll no','please select a roll no  should be selected ')
        return cleaned_data

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('name','contact','city','subject','class_teacher_of')

class AdminForm(ModelForm):
    class Meta:
        model = hod
        fields = ('contact','name')  
        