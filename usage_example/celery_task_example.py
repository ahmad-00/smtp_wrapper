from usage_example import mail_example
from celery import shared_task


@shared_task(bind=True, max_retries=4)
def send_email(self, email_method, **kwargs):
    email_obj = getattr(mail_example, email_method)(**kwargs)
    email_obj.send()
