# Generated by Django 5.0.7 on 2024-07-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_alter_student_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
