from datetime import datetime
from util.mail.strategy import EmailStrategy


class EmailBuilder:
    def __init__(self):
        self.email = Email()

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

    def build(self):
        return self.email

class Email:
    def __init__(self):
        self.strategy = None
        self.sender_email = None
        self.app_password = None
        self.recipient_email = None
        self.subject = None
        self.body = None

    def send(self):
        if self.strategy:
            try:
                # Send the email
                self.strategy.send_email(
                    self.sender_email, self.app_password, self.recipient_email, self.subject, self.body
                )

                # Return success status and timestamp
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
                # Return failure status and error details
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
            # Return failure status if strategy is not set
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
