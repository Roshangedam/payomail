from payomail.core import mail,strategy
from payomail.template.template import HTMLTemplate


if __name__ == "__main__":
    roshan = (
        mail.EmailBuilder()
        .set_strategy(strategy.GmailStrategy())  
        .set_sender("sender@example.com")
        .set_password("SenderPassowrd")
        .build()
    )

    roshan.set_max_attachment_size(10)
    roshan.set_subject("Mail from payomail")
    roshan.set_body('')
    roshan.set_body_from_template(HTMLTemplate()
                                  .set_file_path('payomail/template/test.html')
                                  .set_value('greeting','hello bholya')
                                  .set_value('from','Payomail developer'))
    roshan.attach_file('payomail/images/icon.png')
    roshan.set_recipient("recipient@example.com")
    res=roshan.send()

    print(res)