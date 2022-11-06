from celery import shared_task

from usage_example import email_template


@shared_task(bind=True)
def send_email(self, email_type, **kwargs):
    email_obj = getattr(email_template, email_type)(**kwargs)
    email_obj.send()
