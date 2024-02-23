from payomail import mail
from payomail import strategy


if __name__ == "__main__":
    roshan = (
        mail.EmailBuilder()
        .set_strategy(strategy.IceWarpStrategy())  
        .set_sender("rgedam@microproindia.com")
        .set_password("Pass@1234")
        .build()
    )

    roshan.set_subject("Test")
    roshan.set_body("yetsing 1")
    roshan.set_attachments(['https://lablab.ai/_next/image?url=https%3A%2F%2Fimagedelivery.net%2FK11gkZF3xaVyYzFESMdWIQ%2F6c56e928-3848-4367-5d6b-3006afe68300%2Ffull&w=3840&q=75'])
    roshan.set_recipient("roshangedam1998@gmail.com")


    res=roshan.send()

    print(res)