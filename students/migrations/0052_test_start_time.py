# Generated by Django 5.0.6 on 2024-08-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0051_test_duration_test_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
