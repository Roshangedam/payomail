from abc import ABC, abstractmethod
from email import encoders
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

class EmailStrategy(ABC):
    @abstractmethod
    def send_email(self, sender_email, app_password, recipient_email, subject, body, attachments=None):
        pass

class GmailStrategy(EmailStrategy):
    def send_email(self, sender_email, app_password, recipient_email, subject, body, attachments=None):
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        self._send_email(server, sender_email, recipient_email, subject, body, attachments)

    def _send_email(self, server, sender_email, recipient_email, subject, body, attachments=None):
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        if attachments:
            for attachment in attachments:
                with open(attachment, "rb") as file:
                    part = MIMEApplication(file.read(), Name=basename(attachment))
                part['Content-Disposition'] = f'attachment; filename="{basename(attachment)}"'
                message.attach(part)

        server.sendmail(sender_email, recipient_email, message.as_string())

class IceWarpStrategy(EmailStrategy):
    def send_email(self, sender_email, app_password, recipient_email, subject, body, attachments):
        smtp_server = "mail.microproindia.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        self._send_email(server, sender_email, recipient_email, subject, body, attachments)

    def _send_email(self, server, sender_email, recipient_email, subject, body, attachments):
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        for attachment in attachments:
            with open(attachment, "rb") as file:
                part = MIMEApplication(file.read(), Name=attachment.split("/")[-1])
                part['Content-Disposition'] = f'attachment; filename="{attachment.split("/")[-1]}"'
                message.attach(part)

        server.sendmail(sender_email, recipient_email, message.as_string())