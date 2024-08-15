from datetime import timedelta ,datetime
from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.task import *

class Command(BaseCommand):
    help='Succed the programd'
    def handle(self, *args, **kwargs):
        user_id=2
        message='user Schedule message '
        eta=datetime.now() +timedelta(minutes=1)
        # send_scheduled_message.apply_async((user_id, message), eta=eta)


        self.stdout.write(self.style.SUCCESS('Successfully scheduled message for user_id %d' % user_id))
