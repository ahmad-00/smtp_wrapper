from base_email import BaseHTMLEmail


class SomeEmail(BaseHTMLEmail):
    subject: str = "Some subject"
    message: str = "Some message"

    def __init__(self, recipient_email: str, recipient_name: str):
        self.recipient_email = recipient_email
        self.recipient_name = recipient_name
        super(SomeEmail, self).__init__()
