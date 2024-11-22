from django.shortcuts import render
from django.db.models import Count
from students.models import Classes
# Create your views here.
def admin_panel(request):
    class_data = (
        Classes.objects.annotate(student_count=Count('classgroup__student'))
        .values('name', 'student_count')
    )
    
    # Prepare data for the chart
    labels = [item['name'] for item in class_data]
    series = [item['student_count'] for item in class_data]
    content={
        "labels": labels,
        "series": series,
    }
    return render(request, 'panel/admin_panel.html',content)