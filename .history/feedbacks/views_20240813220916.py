from django.shortcuts import render,redirect,get_object_or_404
from .forms import feedbackform 
from django.contrib.auth.decorators import login_required 
from students.models import Student ,Feedback
from django.template.defaulttags import register    
from django.utils import timezone
from django.db.models import Q
from .forms import FeedbackQuestionForm, FeedbackOptionForm,feedbackCategroryform
from students.models import FeedbackQuestion, FeedbackOption,FeedbackCategory  ,FeedbackResponse
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
    categerory=FeedbackCategory.objects.all()
    duration=make_dictonery(feedbacks)  
    content={'feedbacks':feedbacks ,"duration":duration,"categerory":categerory}
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

def feedback_by_category(request, category_id):
    category = get_object_or_404(FeedbackCategory, id=category_id)
    questions = category.feedbackquestion_set.all()
    responses = FeedbackResponse.objects.filter(Q(question__category=category) Q(response_likert))
    content= {
        'category': category,
        'questions': questions,
        'responses': responses
    }
    return render(request, 'feedbacks/feedback_by_category.html',content)
def create_categerory(request):
    form=feedbackCategroryform()
    if request.method == "POST":
        form=feedbackCategroryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-feedbacks')
    content={"form":form}
    return render(request,"feedbacks/create_categerory.html",content)

def add_question(request,category_id):
    category=FeedbackCategory.objects.get(id=category_id)
    if request.method == 'POST':
        question_form = FeedbackQuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.category=category
            question.save()
            if question.question_type == 'mcq':
                for option_text in request.POST.getlist('options'):
                    FeedbackOption.objects.create(question=question, option_text=option_text)
            return redirect('categerory-feedback',category_id=category_id)  # Redirect to a page showing the list of questions
    else:
        question_form = FeedbackQuestionForm()
    return render(request, 'feedbacks/add_question.html', {'question_form': question_form})

def add_option(request, question_id):
    question = get_object_or_404(FeedbackQuestion, pk=question_id)
    if request.method == 'POST':
        option_form = FeedbackOptionForm(request.POST)
        if option_form.is_valid():
            option = option_form.save(commit=False)
            option.question = question
            option.save()
            return redirect('question_list')
    else:
        option_form = FeedbackOptionForm()
    return render(request, 'feedbacks/add_option.html', {'option_form': option_form, 'question': question})

def submit_feedback(request, category_id):
    category = get_object_or_404(FeedbackCategory, id=category_id)
    questions = FeedbackQuestion.objects.filter(category=category)
    
    if request.method == 'POST':
        user = request.user
        for question in questions:
            response_text = None
            response_choice = None
            response_likert = None
            
            if question.question_type == 'text':
                response_text = request.POST.get(f'question_{question.id}_text')
            elif question.question_type == 'mcq':
                response_choice = request.POST.get(f'question_{question.id}_choice')
            elif question.question_type == 'likert':
                response_likert = request.POST.get(f'question_{question.id}_likert')
                if response_likert == '':  # Handle the empty case
                   response_likert = 0

            FeedbackResponse.objects.create(
                question=question,
                user=user,
                response_text=response_text,
                response_choice=response_choice,
                response_likert=response_likert
            )
        return redirect('list-feedbacks')
    
    return render(request, 'feedbacks/submit_feedback.html', {'category': category, 'questions': questions})