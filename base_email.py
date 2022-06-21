from config import Config
from smtp_client import SMTPClient


class BaseEmail:
    smtp = None
    subject = None
    sender = None
    receiver = None
    html_body = None

    def __init__(self, receiver: str):
        if not receiver or receiver == "":
            return
        self.smtp = SMTPClient()
        self.receiver = receiver
        self.smtp.set_subject(subject=self.subject)
        self.smtp.set_sender(sender=self.sender if self.sender is not None else Config.SMTP_USER)
        self.smtp.set_receiver(receiver=self.receiver)
        self.smtp.set_html_body(body=self.html_body)

    def send(self):
        self.smtp.send()
