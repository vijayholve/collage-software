# Generated by Django 5.0.7 on 2024-07-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_attendance_teacher_attendance_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(blank=True, null=True, to='students.subject'),
        ),
    ]
