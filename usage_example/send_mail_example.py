from celery_task_example import send_email
from usage_example.mail_example import SomeEmail


class SendMailExample:
    def send_some_mail(self, **kwargs):
        send_email.delay(
            SomeEmail.__name__, **kwargs
        )
