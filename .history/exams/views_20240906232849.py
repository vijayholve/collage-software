from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.shortcuts import render, redirect ,get_object_or_404
from .forms import ExamsForm,QuestionForm,OptionForm,AnswerForm
from students.models import Test ,Question,Option ,StudentAnswer,StudentScore ,Student
from django.contrib.messages import error
from django import template 
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta
register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key): 
    return dictionary.get(key)
# Create your views here.
@login_required(login_url="login-page")
def create_exams(request):  
    form = ExamsForm()
    if request.method == "POST":
        form=ExamsForm(request.POST)  
        if form.is_valid():
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            if start_time and end_time:
                test_date = form.cleaned_data.get('test_date')
                start_datetime = datetime.combine(test_date, start_time)
                end_datetime = datetime.combine(test_date, end_time)
                if end_datetime < start_datetime:
                    end_datetime += timedelta(days=1) 
                duration = end_datetime - start_datetime 
                exams = form.save(commit=False)
                exams.duration = duration
                exams.save()
                return redirect('test_detail', pk=exams.pk)
            else:
                form.add_error(None, "Both start time and end time must be provided.")
        
    return render(request,"exams/exam_form.html",{"form":form})
def update_exams(request,test_id):
    test=Test.objects.get(id=test_id)
    form=ExamsForm(instance=test)
    if request.method == "POST":
        form=ExamsForm(request.POST,instance=test)
        if form.is_valid(): 
            form.save()
            return redirect('exam-home')
        else:
            error(request,"Deta is not valid")
    return render(request,"exams/exam_form.html",{"form":form})
@login_required(login_url="login-page")
def home_exams(request):
    now = datetime.now()
    date = now.date()
    time = now.time()
    
    # Query for upcoming exams
    upcoming_tests = Test.objects.filter(test_date__gt=date) | Test.objects.filter(test_date=date, end_time__gt=time)
    upcoming_tests = upcoming_tests.order_by('test_date', 'start_time')
    
    # Query for ended exams
    ended_tests = Test.objects.filter(test_date__lt=date) | Test.objects.filter(test_date=date, end_time__lte=time)
    ended_tests = ended_tests.order_by('-test_date', '-end_time')
    # Combine the querysets
    tests = list(upcoming_tests) + list(ended_tests)
    
    content = {'tests': tests, "now": now, 'date': date}
    return render(request, 'exams/tests_home.html', content)
def delete_exam(request,exam_id):
    exam=Test.objects.get(id=exam_id)
    exam.delete()
    return redirect('exam-home')

def add_question_option(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        option_forms = [OptionForm(request.POST, prefix=str(i)) for i in range(4)]
        if question_form.is_valid() and all([option_form.is_valid() for option_form in option_forms]):
            question = question_form.save(commit=False)
            question.test = test
            question.save()
            for option_form in option_forms:
                option = option_form.save(commit=False)
                option.question = question
                option.save()
            return redirect('test_detail', pk=test.pk)
    else:
        question_form = QuestionForm()
        option_forms = [OptionForm(prefix=str(i)) for i in range(4)]
    content={'question_form': question_form, 'option_forms': option_forms, 'test': test}
    return render(request, 'exams/add_question.html', content) 

def test_detail(request, pk):
    test = Test.objects.get(pk=pk) 
    return render(request, 'exams/test_detail.html', {'test': test}) 
@login_required(login_url="login-page")
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    student = request.user  # Assuming the student is the logged-in user
    questions = test.questions.all()
    student_scrore=students
    if student in 
    
    if request.method == 'POST':
        score = 0
        total_questions = test.questions.count()
        unanswered_questions = []
        
        for question in test.questions.all():
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id is None:
                unanswered_questions.append(question.text)
            else:
                selected_option = get_object_or_404(Option, id=selected_option_id)
                is_correct = selected_option.is_correct

                StudentAnswer.objects.create(
                    student=student,
                    question=question,
                    selected_option=selected_option,
                    is_correct=is_correct
                )

                if is_correct:
                    score += 1
        
        if unanswered_questions:
            messages.error(request, f"You have not answered all the questions. Please answer questions: ( {', '.join(map(str, unanswered_questions))} )")
            return render(request, 'exams/take_test.html', {'test': test, 'questions': questions})

        # Use get_or_create to avoid duplicate entries
        student_score, created = StudentScore.objects.get_or_create(
            student=student,
            test=test,
            defaults={'score': score}
        )

        # If the score already exists, update it
        if not created:
            student_score.score = score
            student_score.save()

        return redirect('students-results', test_id=test_id)

    return render(request, 'exams/take_test.html', {'test': test, 'questions': questions})
def update_quistion(request,quistion_id):
    quistion=Question.objects.get(id=quistion_id)
    test = get_object_or_404(Test, pk=quistion.test.id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, instance=quistion)
        option_forms = [OptionForm(request.POST, instance=opt, prefix=str(opt.id)) for opt in quistion.options.all()]
        
        if question_form.is_valid() and all(option_form.is_valid() for option_form in option_forms):
            question = question_form.save(commit=False)
            question.test = test
            question.save()
            
            for option_form in option_forms:
                option = option_form.save(commit=False)
                option.question = question
                option.save()
            
            return redirect('test_detail',pk=test.id)  # Redirect to a view after a successful update
    
    else:
        question_form = QuestionForm(instance=quistion)
        option_forms = [OptionForm(instance=opt, prefix=str(opt.id)) for opt in quistion.options.all()]
    
    return render(request, 'exams/update_quistion.html', {'question_form': question_form, 'option_forms': option_forms, 'test': test})


def students_result_exam(request,test_id):
    test=Test.objects.get(id=test_id)
    students_scores = StudentScore.objects.filter(test=test).order_by('-score')

    students_details = {}
    for student_score in students_scores:
            # Debugging information
        # print(f"Processing student score: {student_score}")
        # print(f"CustomUser ID: {student_score.student.id}")

        try:
            student = Student.objects.get(user=student_score.student)
            students_details[student_score.student.id] = {
                'name':student.name,
                'roll_no':student.roll_no
            }
        except Student.DoesNotExist:
            
            students_details[student_score.student.id] ={
                'name': 'Unknown',
                'roll_no': 'Unknown'
                                                         }
#  result for debugging
    content = {
        "students_scores": students_scores,
        "test": test,
        "students_details": students_details
    } 
    return render(request, "exams/students_scrore.html", content)
 

def option_delete(request,id,test_id):
    
    option = get_object_or_404(Option, id=id)
    option.delete()
    return redirect('test_detail', pk=test_id )
def quistion_delete(request,id):
    
    quistion = get_object_or_404(Question, id=id)
    test=quistion.test
    quistion.delete()
    return redirect('test_detail', pk=test.id )