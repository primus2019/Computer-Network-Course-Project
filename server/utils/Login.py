import re

from poplib import POP3_SSL
# from server.utils.Mails import *
from utils import Mails
# from Mails import *


def login(login_info=None, test=False):
    try:
        if login_info is None:
            login_info = ask()
        mailserver = re.search(r'@(.*?)\.com', login_info['account'], flags=re.IGNORECASE).group(1)
        if mailserver == '163':
            login_info['pop_host']  = 'pop.163.com'
            login_info['smtp_host'] = 'smtp.163.com'
            login_info['port']      = 25
        else:
            print('unknown mail server: {}'.format(mailserver))
            quit()
        if test:
            login_info = {
                'pop_host':      'pop.163.com',
                'smtp_host':     'smtp.163.com',
                'port':          25,
                'account':     'primus1998@163.com',
                'password':      'jlc123456'
            }
        mail_link = POP3_SSL(login_info['pop_host'])
        mail_link.set_debuglevel(0)
        mail_link.user(login_info['account'])
        mail_link.pass_(login_info['password'])
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
        'account':        '',
        'password':         ''
    }

    for key, value in login_info:
        print('enter your ' + key)
        input(value)
    login_info['port'] = (int)(login_info['port'])

    return login_info
