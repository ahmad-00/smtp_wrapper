from base_email import BaseHTMLEmail


class SomeEmail(BaseHTMLEmail):
    subject: str = "Some subject"
    message: str = "Some message"

    def __init__(self, recipient_email: str, recipient_name: str, **kwargs):
        self.recipient_email = recipient_email
        self.recipient_name = recipient_name
        self.html_body = self.template

        for key, value in kwargs.items():
            self.html_body = self.html_body.replace(key, value)
        super(SomeEmail, self).__init__()
