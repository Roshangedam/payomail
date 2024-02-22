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
    roshan.set_recipient("roshangedam1998@gmail.com")


    res=roshan.send()

    print(res)