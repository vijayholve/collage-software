# Generated by Django 5.0.7 on 2024-07-23 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_subject_student_subject_teacher_attendance_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.subject'),
        ),
    ]
