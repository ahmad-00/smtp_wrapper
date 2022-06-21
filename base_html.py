import os


class BaseHTML:
    template = None
    html_template_name = None

    def load_html_template(self):
        template_path = os.path.join('template_dir', self.html_template_name)
        file = open(template_path, "r", encoding='utf-8')
        template = file.read()
        file.close()
        self.template = template
