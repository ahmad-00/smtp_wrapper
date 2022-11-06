import re

from django.template.loader import render_to_string

from config import Config
from smtp_client import SMTPClient


class BaseEmail:
    _smtp = None
    subject: str
    sender: str
    recipient_email: str
    html_body: str
    _email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self):
        if not self.is_valid_email():
            return
        self._smtp = SMTPClient()
        self._smtp.set_subject(subject=self.subject)
        self._smtp.set_sender(sender=self.sender if self.sender is not None else Config.SMTP_USER)
        self._smtp.set_receiver(receiver=self.recipient_email)
        self._smtp.set_html_body(body=self.html_body)

    def is_valid_email(self):
        if re.fullmatch(self._email_regex, self.recipient_email):
            return True
        return False

    def send(self):
        self._smtp.send()


class BaseHTMLEmail(BaseEmail):
    html_template_name: str = 'base_template.html'
    recipient_name: str
    message: str
    url: str

    def __init__(self):
        """
        Modify context parameters based on your HTML template
        """

        self.html_body = render_to_string(
            self.html_template_name, context={
                'subject': self.subject,
                'message': self.message
            }
        )
        super(BaseHTMLEmail, self).__init__()
