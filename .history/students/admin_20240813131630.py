from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

data=[
  CustomUser,Student,
      Teacher,
      Attendance,
      hod,
    ClassGroup,
    Assignment ,
    Feedback,
    Test,
   
Question,
Option,
StudentAnswer,
StudentScore,
TestResult,
    FeedbackCategory
FeedbackQuestion
FeedbackOption
FeedbackResponse
]

for model in data:
    admin.site.register(model)
