from django.shortcuts import render,redirect
from .forms import feedbackform 
from django.contrib.auth.decorators import login_required 
from students.models import Student ,Feedback
from django.template.defaulttags import register    
from django.utils import timezone
# Create your views here.

def make_dictonery(list_obj):
    return {obj.id : time_since(obj.created_at) for obj in list_obj}
@login_required(login_url="login-page")
def create_feedback(request):
    forms=feedbackform() 
    
    if request.method == "POST":  
        forms=feedbackform(request.POST) 
        if forms.is_valid():  
            feedback = forms.save(commit=False)
            feedback.student = request.user  # Set the student field to the logged-in user
            feedback.save()     
            return redirect('home') 
    content={'forms':forms} 
    return render(request,"feedbacks\create_feedback.html",content)  
@register.filter
def get_item(dictionery,key):
    return dictionery.get(key)
@login_required(login_url="login-page")
def list_feedbacks(request):
    feedbacks=Feedback.objects.all()
    duration=make_dictonery(feedbacks)  
    content={'feedbacks':feedbacks ,"duration":duration}
    return render(request,"feedbacks\list_feedbacks.html",content)  # Render the template with the feedbacks list

@register.filter
def time_since(value):
    now=timezone.now()
    diff=now-value
    if diff.days == 0:
        if diff.seconds >= 0 and diff.seconds < 60:
            return 'just now'
        if diff.seconds >= 60 and diff.seconds < 3600:
            minutes = diff.seconds // 60
            return f'{minutes} minutes ago'
        if diff.seconds >= 3600 and diff.seconds < 86400:
            hours = diff.seconds // 3600
            return f'{hours} hours ago'
    if diff.days == 1:
        return 'yesterday'
    if diff.days < 7:
        return f'{diff.days} days ago'
    if diff.days < 30:
        weeks = diff.days // 7
        return f'{weeks} weeks ago'
    if diff.days < 365:
        months = diff.days // 30
        return f'{months} months ago'
    years = diff.days // 365
    return f'{years} years ago'