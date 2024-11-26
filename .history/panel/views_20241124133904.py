from django.shortcuts import render
from django.db.models import Count
from students.models import Classes,Attendance, Classes,Student,Teacher,Holiday
# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

@login_required(login_url="login-page") 
def admin_panel(request):
    number_of_students = Student.objects.count()
    class_data = (
        Classes.objects.annotate(student_count=Count('classgroup__student'))
        .values('name', 'student_count')
    )

    # Prepare data for the chart
    labels = [item['name'] for item in class_data]
    series = [item['student_count'] for item in class_data]

    class_attendance = []
    classes = Classes.objects.all()
    start_date = datetime(2024, 6, 1)
    end_date = datetime(2025, 5, 1)

    # Calculate all Sundays and other holidays in the date range
    holidays = list(Holiday.objects.filter(date__range=(start_date, end_date)).values_list('date', flat=True))

    # Add all Sundays within the range to the holidays list
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 6:  # Sunday
            holidays.append(current_date)
        current_date += timedelta(days=1)

    holidays = list(set(holidays))  # Remove duplicates
    total_holidays = len(holidays)

    for cls in classes:
        # Count students related to the class
        total_students = cls.classgroup_set.values_list('student', flat=True).count()
        if total_students > 0:
            # Use the id instead of name for filtering
            total_days = (end_date - start_date).days + 1
            effective_days = total_days - total_holidays

            # Filter attendance records within the date range
            total_present = Attendance.objects.filter(
                student__classgroup__name_id=cls.id,
                present=True,
                date__range=(start_date, end_date)
            ).count()

            total_absent = (effective_days * total_students) - total_present

            class_attendance.append({
                'class_name': cls.name,
                'present': total_present,
                'absent': total_absent
            })

    # Extract data for chart
    categories = [item['class_name'] for item in class_attendance]
    present_series = [item['present'] for item in class_attendance]
    absent_series = [item['absent'] for item in class_attendance]

    teachers = Teacher.objects.all()
    content = {
        "labels": labels,
        "series": series,
        'categories': categories,
        'present_series': present_series,
        'absent_series': absent_series,
        "number_of_students": number_of_students,
        "teachers": teachers,
        "classes": classes,
        "total_holidays": total_holidays,
    }
    return render(request, 'panel/admin_panel.html', content)