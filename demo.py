from poplib import POP3_SSL
import os
import re
import Basics

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


def mailBoxInfo(mail_link):
    '''extract the number of mails in box

    '''

    try:
        mail_list = mail_link.list()[1]
        if len(mail_list) == 0:
            print('No mail in box!')
            return
        mail_info = mail_list[0].split(b' ')
        number = mail_info[0]
        mail = mail_link.retr(number)[1]

        print('mail_info: ' + (str)(mail_info))
        print('number: '    + (str)(number))
        print('mail: '      + (str)(mail))
    except Exception as e:
        print((str)(e))
        return



def retrMail(mailLink, retr_num=0):
    '''retr existing mails in the logged mailbox

    '''
    clearLog()
    try:
        # only 1# element is useful; see mail_info.log
        mail_list = [[(int)(mail_idx), (int)(mail_myth)] for mail_idx, mail_myth in (item.decode('utf-8').split(' ') for item in mailLink.list()[1])]
        for file_name in os.listdir('log/'):
            if file_name.endswith('.log'):
                os.remove('log/' + (str)(file_name))
        for i in range(1, 10):
            open('log/mail_' + (str)(i) + '.log', 'w+').close()
        if retr_num == 0:
            retr_num = mail_list[-1][0]
        if len(mail_list) == 0:
            return None
        # number = mail_info[0]
        # mail = mailLink.retr(number)[1]
        for i in range(1, retr_num):
            mail_info = [info.decode('utf-8') for info in mailLink.retr(i)[1:][0]]
            # for info in mailLink.retr(i)[1:][0]:
            #     # print('##############################' + info.decode('utf-8'))
            #     mail_info.append(info.decode('utf-8'))
            Basics.getInfo(mail_info)
            
            # with open('log/mail_' + (str)(i) + '.log', 'a+', encoding='utf-8') as file:
            #     for info in mailLink.retr(i)[1:][0]:
            #         file.write(info.decode('utf-8'))
            #         file.write('\n')
            # with open('log/mail_' + (str)(i) + '.log', 'r+', encoding='utf-8') as file:
            #     content = file.read().splitlines()
            #     print('file: ' + (str)(i))
            #     for line in content:
            #         obj_cc              = re.search(r'(?:cc:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',     line, flags=re.IGNORECASE)
            #         obj_subject         = re.search(r'(?:subject:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',line, flags=re.IGNORECASE)
            #         obj_to              = re.search(r'(?:to:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',     line, flags=re.IGNORECASE)
            #         obj_from            = re.search(r'(?:from:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',   line, flags=re.IGNORECASE)
            #         obj_date            = re.search(r'(?:date:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',   line, flags=re.IGNORECASE)
            #         obj_content_type    = re.search(r'(?:content-type:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*(?:format:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*', line, flags=re.IGNORECASE)
            #         obj_charset         = re.search(r'(?:charset:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',line, flags=re.IGNORECASE)
            #         obj_transfer_encoding = re.search(r'(?:content-transfer-encoding:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*', line, flags=re.IGNORECASE)
            #         obj_boundary        = re.search(r'(?:boundary=\s*[\'\"]*([^\'\";]*)[\'\";]*)', line, flags=re.IGNORECASE)
            #         # if obj_from.group(1) is not None:
            #         #     print('from: '                      + obj_from.group(1))
            #         # if obj_to.group(1) is not None:
            #         #     print('to: '                        + obj_to.group(1))
            #         # if obj_cc.group(1) is not None:
            #         #     print('cc: '                        + obj_cc.group(1))
            #         # if obj_date.group(1) is not None:
            #         #     print('date: '                      + obj_date.group(1))
            #         # if obj_content_type.group(1) is not None:
            #         #     print('content-type: '              + obj_content_type.group(1))
            #         # if obj_charset.group(1) is not None:
            #         #     print('charset: '                   + obj_charset.group(1))
            #         # if obj_transfer_encoding.group(1) is not None:
            #         #     print('content-transfer-encoding: ' + obj_transfer_encoding.group(1))
            #         if obj_boundary is not None:
            #             print('boundary: '                    + obj_boundary.group(1))
                    
            print('-------------------------------------------')
        return None
    except Exception as e:
        print(str(e))
        return None


def clearLog():
    for file_name in os.listdir('log/'):
        if file_name.endswith('.log'):
            os.remove('log/' + (str)(file_name))

if __name__ == '__main__':
    mail_link = login()
    # mailBoxInfo(mail_link)
    retrMail(mail_link)