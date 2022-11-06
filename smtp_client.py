import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from hiamooz.config import Config


class SMTPClient:
    message = None

    def __init__(self):
        self.smtp = smtplib.SMTP_SSL(
            host=Config.SMTP_HOST,
            port=Config.SMTP_PORT
        )

        self.smtp.login(
            user=Config.SMTP_USER,
            password=Config.SMTP_PASSWORD
        )

        self.message = MIMEMultipart('alternative')

    def set_subject(self, subject):
        self.message['subject'] = subject

    def set_sender(self, sender: str):
        self.message['from'] = sender

    def set_receiver(self, receiver: str):
        self.message['to'] = receiver

    def set_html_body(self, body):
        self.message.attach(MIMEText(body, 'html'))

    def send(self):
        try:
            self.smtp.sendmail(
                from_addr=self.message['from'],
                to_addrs=self.message['to'],
                msg=self.message.as_string()
            )
        finally:
            self.smtp.quit()
