# PayoMail - Open Source Email Sending Utility ✉️

PayoMail is an open-source Python utility for sending emails with different email providers. It provides a flexible architecture supporting various email strategies and a convenient interface for configuring and sending emails.

## Features 🚀

- **Modular Architecture:** Choose from different email strategies like Gmail, IceWarp, etc.
- **Builder Pattern:** Easily configure and customize emails using a builder pattern.
- **Template Support:** Support for email templates with dynamic values.
- **File Attachment:** Attach files from local paths or URLs.

## Getting Started 🛠️

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites 📋

- Python 3.x

### Installation 📦

1. Clone the repository:

    ```bash
    git clone https://github.com/Roshangedam/payomail.git
    ```

2. Navigate to the project directory:

    ```bash
    cd payomail
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Installation via pip 📦

PayoMail is available on PyPI, the Python Package Index. You can install it using pip:

```bash
pip install payomail
```

### Usage 🖥️

```python
# Your Python script

from payomail.core import mail, strategy
from payomail.template.template import HTMLTemplate


if __name__ == "__main__":
    # Create an email builder object
    roshan = (
        mail.EmailBuilder()
        .set_strategy(strategy.GmailStrategy())  
        .set_sender("sender@example.com")
        .set_password("SenderPassword")
        .build()
    )

    # Set maximum attachment size
    roshan.set_max_attachment_size(10)

    # Set email subject
    roshan.set_subject("Mail from PayoMail")

    # Set email body from HTML template use {{mapping}} and mapp value of html with .set_value('mapping', 'some value')
    roshan.set_body_from_template(HTMLTemplate()
                                  .set_file_path('payomail/template/test.html')
                                  .set_value('greeting', 'Hello Bholya')
                                  .set_value('from', 'PayoMail Developer'))

    # Attach an image file single multiple with file path or url
    roshan.attach_file('payomail/images/icon.png')
    #roshan.attach_file('https://com.example/somefile.file')

    # Set recipient email address
    roshan.set_recipient("recipient@example.com")

    # Send the email
    response = roshan.send()
    
    # Displaying the response details
    print(f"Status: {response['status']}")
    print(f"From: {response['from']}")
    print(f"To: {response['to']}")
    print(f"Subject: {response['subject']}")
    print(f"Timestamp: {response['timestamp']}")

    # If there was a failure, print the error message
    if response['status'] == 'Failure':
        print(f"Error Message: {response['error_message']}")

```

## Contributing 🤝

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License 📄

This project is licensed under the [License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 🙌

- Hat tip to anyone whose code was used
- Inspiration
- etc.

This version of PayoMail supports email templates with dynamic values using the `HTMLTemplate` class. You can attach files from local paths or URLs using the `attach_file` method.