from base_email import BaseEmail
from base_html import BaseHTML


class SomeEmail(BaseEmail, BaseHTML):
    subject = 'Email Subject'
    html_template_name = 'some_template.html'

    def __init__(self, receiver: str, **kwargs):
        self.load_html_template()
        # You can modify your html file here
        super(SomeEmail, self).__init__(receiver=receiver, **kwargs)
