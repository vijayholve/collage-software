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
   Timetable,
   TimeSlot,
Question,
Option,
StudentAnswer,
StudentScore,
AssignmentSubmission,
TestResult,
    FeedbackCategory,
FeedbackQuestion,
FeedbackOption,
FeedbackResponse,

]

for model in data:
    admin.site.register(model)
