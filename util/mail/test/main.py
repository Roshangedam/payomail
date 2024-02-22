from util.mail.mail import EmailBuilder
from util.mail.strategy import IceWarpStrategy


if __name__ == "__main__":
    roshan = (
        EmailBuilder()
        .set_strategy(IceWarpStrategy())  
        .set_sender("email@example.com")
        .set_password("password")
        .build()
    )

    roshan.set_subject("Test Email")
    roshan.set_body(
"select * from r_cvrsrv_dtl t where t.rcsd_cvrno='1629059';\n" +
"\n" + 
"select * from pi_emp_hdr t where t.pieh_empid = (select m.adum_user_id from ad_user_mst m where m.adum_name = 'JALA MARINALEENA')"
)
    roshan.set_recipient("roshangedam1998@gmail.com")


    res=roshan.send()

    print(res)