from poplib import POP3_SSL
import os
import re


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


def retrMail(mailLink, retr_num):
    '''retr existing mails in the logged mailbox

    '''
    try:
        mail_list = mailLink.list()[1]
        if len(mail_list) == 0:
            return None
        mail_info = mail_list[0].split(b' ')
        number = mail_info[0]
        # mail = mailLink.retr(number)[1]
        for i in range(1, retr_num):
            with open('mail_' + (str)(i) + '.log', 'a+', encoding='utf-8') as file:
                for info in mailLink.retr(i)[1:][0]:
                    file.write(info.decode('utf-8'))
                    file.write('\n')
            with open('mail_' + (str)(i) + '.log', 'r+', encoding='utf-8') as file:
                content = file.read().splitlines()
                print('file: ' + (str)(i))
                for line in content:
                    loc_content_type = line.find('Content-Type: ')
                    loc_date    = line.find('Date: ')
                    loc_from    = line.find('From: ')
                    loc_to      = line.find('To: ')
                    loc_subject = line.find('Subject: ')
                    loc_cc      = line.find('Cc: ')
                    obj_content_type = re.match(r'Content-Type: (.*);', line, re.M|re.I)
                    if obj_content_type != None:
                        print(obj_content_type.group(1))
                    # if loc_content_type != -1:
                    #     print('content-type:' + line[loc_content_type + 14:])
                    # if loc_date != -1:
                    #     print(' date:       ' + line[loc_date + 6:])
                    # if loc_from != -1:
                    #     print(' from:       ' + line[loc_from + 6:])
                    # if loc_to != -1:
                    #     print(' to:         ' + line[loc_to + 4:])
                    # if loc_subject != -1:
                    #     print(' subject:    ' + line[loc_subject + 9:])
                    # if loc_cc != -1:
                    #     print('cc:          ' + line[loc_cc + 4])
        return None
    except Exception as e:
        print(str(e))
        return None


if __name__ == '__main__':
    retr_num = 19

    for i in range(1, 10):
        open('mail_' + (str)(i) + '.log', 'w+').close()
    mailLink = login()
    print(retrMail(mailLink, retr_num))