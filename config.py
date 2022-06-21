import os


class Config:
    """
    Only static config data must be placed here.
    Config properties are usually loaded from .env file
    Your project probably has different structure for loading config files, in that case you can remove this class and replace used properties properly.
    """

    SMTP_USER = os.environ.get('SMTP_USER')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
    SMTP_HOST = os.environ.get('SMTP_HOST')
    SMTP_PORT = int(os.environ.get('SMTP_PORT'))
