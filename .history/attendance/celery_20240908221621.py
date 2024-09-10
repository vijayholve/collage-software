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
        'task': 'students.task.hello',
        'schedule': crontab(hour=22, minute=16),
        },
}

@app.task(bind=True)
<<<<<<< Tabnine <<<<<<<
@shared_task(bind=True)#+
def hello(self):#+
    """#+
    This function prints "hello" 9 times using a for loop.#+
#+
    Parameters:#+
    self (celery.app.task.Task): The current task instance. This parameter is automatically passed by Celery when the task is executed.#+
#+
    Returns:#+
    None: This function does not return any value.#+
    """#+
    for i in range(1,10):#+
        print("hello")#+
>>>>>>> Tabnine >>>>>>>
def bind_fun(self):
    print(f"Request: {self.request!r}")
