from abc import ABC, abstractmethod
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailStrategy(ABC):
    @abstractmethod
    def send_email(self, sender_email, app_password, recipient_email, subject, body):
        pass

class GmailStrategy(EmailStrategy):
    def send_email(self, sender_email, app_password, recipient_email, subject, body):
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        self._send_email(server, sender_email, recipient_email, subject, body)

    def _send_email(self, server, sender_email, recipient_email, subject, body):
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_email, message.as_string())

class IceWarpStrategy(EmailStrategy):
    def send_email(self, sender_email, app_password, recipient_email, subject, body):
        smtp_server = "mail.microproindia.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        self._send_email(server, sender_email, recipient_email, subject, body)

    def _send_email(self, server, sender_email, recipient_email, subject, body):
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_email, message.as_string())