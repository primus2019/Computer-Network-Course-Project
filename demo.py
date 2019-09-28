from poplib import POP3_SSL
import os
import re
from BackEnd import BackEnd
from BackEnd.Operations import Login
from FrontEnd.BasicFrame import Root, Application

test_info = {
    'pop_host':      'pop.163.com',
    'smtp_host':     'smtp.163.com',
    'port':          25,
    'user_name':     'primus1998@163.com',
    'password':      'jlc123456'
}


def clearLog():
    for file_name in os.listdir('log/'):
        if file_name.endswith('.log'):
            os.remove('log/' + (str)(file_name))


if __name__ == '__main__':
    root = Root("1400x700+0+0", 'mailbox demo')
    root.setMax()
    root.tk.call('encoding', 'system', 'utf-8')
    app = Application(master=root)
    app.mainloop()
    # mail_link = Login.login(test_info)
    # # mailBoxInfo(mail_link)
    # retrMail(mail_link, 5)