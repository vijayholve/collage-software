from celery import shared_task
from .seed import assignement_have_to_send_msg

@shared_task(bind=True)
def send_mail_to_all_students_for_assignemt(self,id):
    assignement_have_to_send_msg(id)
    return "done"