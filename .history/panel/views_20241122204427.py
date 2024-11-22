from django.shortcuts import render
from django.db.models import Count
from students.models import Classes,Attendance, Classes
# Create your views here.
def admin_panel(request):
    class_data = (
        Classes.objects.annotate(student_count=Count('classgroup__student'))
        .values('name', 'student_count')
    )
    
    # Prepare data for the chart
    labels = [item['name'] for item in class_data]
    series = [item['student_count'] for item in class_data]
    class_attendance = []
    classes = Classes.objects.all()
    for cls in classes:
        # Count students related to the class
        total_students = cls.classgroup_set.values_list('student', flat=True).count()
        if total_students > 0:
            # Use the id instead of name for filtering
            total_attendance = Attendance.objects.filter(student__classgroup__name_id=cls.id).count()
            total_present = Attendance.objects.filter(
                student__classgroup__name_id=cls.id,
                present=True
            ).count()
            attendance_percentage = (total_present / total_attendance) * 100 if total_attendance else 0
            class_attendance.append({
                'class_name': cls.name,
                'percentage': round(attendance_percentage, 2)
            })
    
    # Extract data for chart
    categories = [item['class_name'] for item in class_attendance]
    series = [item['percentage'] for item in class_attendance]
    content={
        "labels": labels,
        "series": series,
         'categories': categories,
        'serieses': serieses
    }
    return render(request, 'panel/admin_panel.html',content)