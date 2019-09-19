from poplib import POP3_SSL


popHost = 'pop.163.com'
smtpHost = 'smtp.163.com'
port = 25
userName = 'primus1998@163.com'
passWord = 'jlc123456'
bossMail = 'primus1998@163.com'


def login():
    try:
        mailLink = POP3_SSL(popHost)
        mailLink.set_debuglevel(0)
        mailLink.user(userName)
        mailLink.pass_(passWord)
        # print(mailLink.list())
        print('Login successfully!' )
        return mailLink
    except Exception as e:
        print('Login fails!' + str(e))
        quit()


def retrMail(mailLink):
    try:
        mail_list = mailLink.list()[1]
        if len(mail_list) == 0:
            return None
        mail_info = mail_list[0].split(b' ')
        number = mail_info[0]
        # mail = mailLink.retr(number)[1]
        print(mailLink.retr(2))
        
        
        return content
    except Exception as e:
        print(str(e))
        return None


if __name__ == '__main__':
    mailLink = login()
    print(retrMail(mailLink))