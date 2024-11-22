from django.shortcuts import render

# Create your views here.
def admin_panel(request):
    class_data = (
        Classes.objects.annotate(student_count=Count('classgroup__student'))
        .values('name', 'student_count')
    )
    
    # Prepare data for the chart
    labels = [item['name'] for item in class_data]
    series = [item['student_count'] for item in class_data]
    return render(request, 'panel/admin_panel.html')