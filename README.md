# PayoMail - Open Source Email Sending Utility ✉️

PayoMail is an open-source Python utility for sending emails with different email providers. It provides a flexible architecture supporting various email strategies and a convenient interface for configuring and sending emails.

## Features 🚀

- **Modular Architecture:** Choose from different email strategies like Gmail, IceWarp, etc.
- **Builder Pattern:** Easily configure and customize emails using a builder pattern.
- **Detailed Responses:** Get detailed responses, including status, sender, recipient, subject, and timestamp.

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

from payomail.mail import EmailBuilder
from payomail.strategy import GmailStrategy

if __name__ == "__main__":
    # Creating and configuring an email using the builder pattern
    email = (
        EmailBuilder()
        .set_strategy(GmailStrategy())
        .set_sender("your_email@gmail.com")
        .set_password("your_app_password")
        .build()
    )

    # Setting subject, body, and recipient after build with adding attachment
    email.set_subject("Test Email")
    email.set_body("This is a test email sent from Python.")
    email.set_recipient("recipient@example.com")
    roshan.attach_file('payomail/images/icon.png')
    roshan.attach_file('https://images.pexels.com/photos/1386604/pexels-photo-1386604.jpeg')
    roshan.attach_file('https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4')
    # Sending the configured email and capturing the response
    response = email.send()

    # Displaying the response details
    print(f"Status: {response['status']}")
    print(f"From: {response['from']}")
    print(f"To: {response['to']}")
    print(f"Subject: {response['subject']}")
    print(f"Timestamp: {response['timestamp']}")

    # If there was a failure, you can also print the error message
    if response['status'] == 'Failure':
        print(f"Error Message: {response['error_message']}")


```
## Contributing 🤝

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License 📄

This project is licensed under the  License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 🙌

- Hat tip to anyone whose code was used
- Inspiration
- etc.
