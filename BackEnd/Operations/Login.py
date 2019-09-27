from poplib import POP3_SSL


def login(test_info=None):
    try:
        if test_info is None:
            test_info = ask()
        mail_link = POP3_SSL(test_info['pop_host'])
        mail_link.set_debuglevel(0)
        mail_link.user(test_info['user_name'])
        mail_link.pass_(test_info['password'])
        # print(mail_link.list())
        print('Login successfully!' )
        return mail_link
    except Exception as e:
        print('Login fails!' + str(e))
        quit()


def ask():
    login_info = {
        'pop_host':         '',
        'smtp_host':        '',
        'port':             '',
        'user_name':        '',
        'password':         ''
    }

    for key, value in login_info:
        print('enter your ' + key)
        input(value)
    login_info['port'] = (int)(login_info['port'])

    return login_info