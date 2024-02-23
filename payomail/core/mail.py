# main code

from datetime import datetime
import os
from typing import  Union
from urllib.parse import urlparse
from payomail.core.strategy import EmailStrategy
from payomail.core.file import download_file, get_size_by_path
from payomail.template.template import HTMLTemplate


class EmailBuilder:
    def __init__(self, default_max_attachment_size_mb=10):
        self.email = Email(default_max_attachment_size_mb)
        self.pending_attachments = []  # to store attachments that are added after building

    def set_strategy(self, strategy: EmailStrategy):
        self.email.strategy = strategy
        return self

    def set_sender(self, sender_email):
        self.email.sender_email = sender_email
        return self

    def set_password(self, app_password):
        self.email.app_password = app_password
        return self

    def set_recipient(self, recipient_email):
        self.email.recipient_email = recipient_email
        return self

    def set_subject(self, subject):
        self.email.subject = subject
        return self

    def set_body(self, body):
        self.email.body = body
        return self

    def set_max_attachment_size(self, max_attachment_size_mb):
        self.email.set_max_attachment_size(max_attachment_size_mb)
        return self
           
    def build(self):
        return self.email


class Email:
    def __init__(self, default_max_attachment_size_mb=10):
        self.strategy = None
        self.sender_email = None
        self.app_password = None
        self.recipient_email = None
        self.subject = None
        self.body = None
        self.html_content=None
        self.attachments = []
        self.max_attachment_size_bytes = default_max_attachment_size_mb * 1024 * 1024  # Default: 10 MB

    def set_max_attachment_size(self, max_attachment_size_mb):
        self.max_attachment_size_bytes = max_attachment_size_mb * 1024 * 1024  # Convert MB to bytes

    def attach_file(self, file_source: Union[str, bytes]):
        if isinstance(file_source, str) and urlparse(file_source).scheme:
            result = download_file(file_source, self.max_attachment_size_bytes)
            if result['status'] == 'Failure':
                print(f"Failed to attach file. Error message: {result['error_message']}")
            self.attachments.append(result['path'])
        else:
            result = get_size_by_path(file_source)
            if result['size'] > self.max_attachment_size_bytes:
               print(f"Failed to attach file. Error message: {result['error_message']}")
               file_source=''
            self.attachments.append(file_source)
        return self


    def send(self):
        if self.strategy:
            try:
                self.strategy.send_email(
                    self.sender_email, self.app_password, self.recipient_email,
                    self.subject, self.body,self.html_content, self.attachments
                )
                self.clean_temp()
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
                response = {
                    'status': 'Success',
                    'from': self.sender_email,
                    'to': self.recipient_email,
                    'subject': self.subject,
                    'timestamp': timestamp
                }
                return response

            except Exception as e:
                self.clean_temp()
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
                response = {
                    'status': 'Failure',
                    'error_message': str(e),
                    'from': self.sender_email,
                    'to': self.recipient_email,
                    'subject': self.subject,
                    'timestamp': timestamp
                }
                return response                                    
        else:
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
            response = {
                'status': 'Failure',
                'error_message': 'Strategy not set. Use set_strategy() to set the email strategy.',
                'from': None,
                'to': None,
                'subject': None,
                'timestamp': timestamp
            }
            return response

    def set_subject(self, subject):
        self.subject = subject
        return self

    def set_body(self, body):
        self.body = body
        return self

    def set_recipient(self, recipient_email):
        self.recipient_email = recipient_email
        return self
    
    def clean_temp(self):
        temp_folder = os.path.join(os.getcwd(), 'payomail', 'temp')
        for attachment in self.attachments:
            try:
                attachment_path = os.path.abspath(attachment)
                if os.path.commonpath([attachment_path, temp_folder]) == temp_folder:
                   os.remove(attachment_path)
            except (FileNotFoundError, OSError):
                   print(f"Error removing file: {attachment}")
   
    def set_body_from_template(self, template):
        """
        Set the email body from a template.

        Parameters:
            template (Template): The template object containing the content.
        """
        if isinstance(template, HTMLTemplate):
            # If the template is an HTML template, set the body accordingly
            self.html_content = template.content
        return self