from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance.settings')

app = Celery('attendance')

# Timezone settings
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

# Load task settings from Django settings with CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in installed apps
app.autodiscover_tasks()

# Celery beat schedule
app.conf.beat_schedule = {
    'print-hello': {
        'task': 'students.task.send_absence_emails',#C:\Users\Vijay\python pro\attendance2\students\task.py
        'schedule': crontab(hour=22, minute=32),
        },
}

@app.task(bind=True)
def bind_fun(self):
    print(f"Request: {self.request!r}")
