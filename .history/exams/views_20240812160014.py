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
def create_exams(request):  
    form = ExamsForm()
    if request.method == "POST":
        form=ExamsForm(request.POST)  
        if form.is_valid():
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')

            if start_time and end_time:
                # Combine start_time and end_time with test_date for duration calculation
                test_date = form.cleaned_data.get('test_date')
                start_datetime = datetime.combine(test_date, start_time)
                end_datetime = datetime.combine(test_date, end_time)

                if end_datetime < start_datetime:
                    end_datetime += timedelta(days=1)  # Handle end time being past midnight

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

def home_exams(request):
    tests=Test.objects.all().order_by('test_date')
    now=datetime.now() 
    date=now.date()
    content={'tests': tests,"now":now,'date':date}
    return render(request,rf'exams\tests_home.html',content )
def delete_exam(request,exam_id):
    exam=Test.objects.get(id=exam_id)
    exam.delete()
    return redirect('exam-home')

def add_question(request, test_id):
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
    questions=test.questions.all()
    if request.method == 'POST':
        score = 0
        total_questions = test.questions.count()

        for question in test.questions.all():
            selected_option_id = request.POST.get(f'question_{question.id}')
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
        # feefback=f"congratulation You scrore is  {student_score.score}/{total_questions} in { test}"
        # content={'score': score, 'total_questions': total_questions, 'test': test,
        #          "created":created}
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
        print(f"Processing student score: {student_score}")
        print(f"CustomUser ID: {student_score.student.id}")

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