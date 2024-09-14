from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime,timedelta  
from django.conf import settings 
class Classes(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} " 
class ClassGroup(models.Model):
    name = models.ForeignKey(Classes,on_delete=models.SET_NULL,null=True)
    year = models.CharField(max_length=100, choices=[('FY', 'First Year'), ('SY', 'Second Year'), ('TY', 'Third Year')])

    def __str__(self):
        return f"{self.name} - {self.year}"
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

class hod(models.Model):
    name=models.CharField(max_length=200)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)       
    contact = models.CharField(max_length=15,null=True ,blank=True) 


class Subject(models.Model):
    name = models.CharField(max_length=100)
    # code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    roll_no=models.IntegerField(unique=True,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True) 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True,blank=True)
    contact = models.CharField(max_length=150,null=True ,blank=True )  
    email=models.EmailField(null=True ,blank=True) 
    subject=models.ManyToManyField(Subject) 
    profile=models.ImageField(upload_to='profile_images/', default=rf"/profile_images/default.jpeg",
                             null=True,blank=True) 
    classgroup=models.ForeignKey(ClassGroup,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return f"{self.id} is {self.name}"  
    def schedule_welcome_message(self):
        # Schedule the task to run 1 minute from now
        eta = datetime.now() + timedelta(minutes=1)
        # send_scheduled_message.apply_async((self.user.id, 'Welcome to our platform!'), eta=eta)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Schedule welcome message after the student is saved
        self.schedule_welcome_message()
    

    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100) 
    contact = models.CharField(max_length=15,null=True ,blank=True)     
    city=models.CharField(max_length=200 ,null=True ,blank=True)  
    subject=models.OneToOneField(Subject,on_delete=models.SET_NULL ,blank=True , null=True)
    class_teacher_of = models.OneToOneField('ClassGroup', on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')
    
    def __str__(self):
        return self.name 
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField() 
    present = models.BooleanField(default=False) 
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True ,blank=True ) 
    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"
class Assignment(models.Model):  
    title = models.CharField(max_length=255) 
    description = models.FileField('assignment_images/') 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    assigned_date = models.DateField(auto_now_add=True) 
    due_date = models.DateField() 
    assigned_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)  
    classgroup=models.ForeignKey(ClassGroup,on_delete=models.SET_NULL, 
                                 null=True,blank=True) 

    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    submitted_date = models.DateField()  
    status = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.assignment.title} - {self.student.name}"

class Test(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True ,null=True,blank=True)  
    test_date = models.DateTimeField() 
    start_time=models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    duration=models.DurationField(null=True,blank=True)
    conducted_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classgroup=models.ForeignKey(ClassGroup,on_delete=models.SET_NULL, 
                                 null=True,blank=True)  
    passing_marks=models.
    def __str__(self):
        return self.title 
class Question(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='questions')
    text=models.TextField(max_length=200) 
    def __str__(self) -> str:
        return f"{self.test} quistion is {self.text}" 
class Option(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="options")
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False) 
    def __str__(self):
        return self.option_text 
class StudentAnswer(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    def save(self, *args, **kwargs):
        if self.selected_option.is_correct:
            self.is_correct = True
        else:
            self.is_correct = False
        super().save(*args, **kwargs)

class StudentScore(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    test = models.ForeignKey(Test, on_delete=models.CASCADE) 
    score = models.PositiveIntegerField(default=0) 
  
    def update_score(self, increment):
        self.score += increment
        self.save()
    
class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.test.title} - {self.student.name}"

class Feedback(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='feedbacks', null=True, blank=True)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.student}'
    

class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField() 
    file=models.FileField(upload_to="books/",null=True,blank=True)
    def __str__(self) -> str:
        return f"name is {self.name}" 
    
class FeedbackCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    
class FeedbackQuestion(models.Model):
    category = models.ForeignKey(FeedbackCategory, on_delete=models.CASCADE)
    question_text = models.TextField()
    QUESTION_TYPE_CHOICES = [
        ('text', 'Text'),
        ('mcq', 'Multiple Choice'),
        ('likert', 'Likert Scale'),
    ]
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPE_CHOICES)

class FeedbackOption(models.Model):
    question = models.ForeignKey(FeedbackQuestion, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)

class FeedbackResponse(models.Model):
    question = models.ForeignKey(FeedbackQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    response_choice = models.CharField(max_length=255, null=True, blank=True)
    response_likert = models.IntegerField(default=0,null=True, blank=True)


from datetime import time
class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.start_time}-{self.end_time}-"
    
    
    
class Timetable(models.Model):
    classgroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE,null=True,blank=True)
    day_of_week = models.CharField(max_length=9, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'), 
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ],null=True)
