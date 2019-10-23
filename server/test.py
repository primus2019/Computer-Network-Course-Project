from utils import Login
from utils import Mails
from utils import Transfer
import os
import email.parser
from email.policy import default


def __test():
    login_info = {
        'pop_host':      'pop.163.com',
        'smtp_host':     'smtp.163.com',
        'port':          25,
        'account':     'primus1998@163.com',
        'password':      'jlc123456'
    }
    mail_link = Login.login(login_info)
    raw_mails = Mails.retrMail(mail_link, 5)
    # print(email.parser.Parser(policy=default).parsestr(text=''.join(raw_mails[0])))
    # # for i, raw_mail in enumerate(raw_mails):
    # #     stringed_raw_email = '\n'.join(raw_mail)
    # #     header_info = email.parser.HeaderParser().parsestr(stringed_raw_email)
    # #     for key, value in header_info.items():
    # #         print('{}: {}'.format(key, Transfer.encode(value)))
        # e = email.message_from_string(stringed_raw_email)
        # if e.is_multipart():
        #     # print('is multipart!')
        #     for j, payload in enumerate(e.walk()):
        #         print((str)(i) + '.' + (str)(j) + ' ' + (str)(payload.get_content_type()))
        # else:
        #     # print('is not multipart!!!!!!!!!!!!!!!!!!!!!!!!')
        #     print((str)(i) + '.' + (str)(0) + ' ' + (str)(e.get_content_type()))


    separated_mails = []
    for i, raw_mail in enumerate(raw_mails): # raw_mail must be string
        separated_mail = []
        raw_mail = '\n'.join(raw_mail)

        header_info = email.parser.HeaderParser().parsestr(raw_mail)
        separated_mail.append({
            key: Transfer.encode(value) for key, value in header_info.items()
        })
        # for i, (key, value) in enumerate(header_info.items()):
        #     separated_mail.append({key: Transfer.encode(value)})
        
        e = email.message_from_string(raw_mail)
        if e.is_multipart():
            # print('is multipart!')
            for payload in e.walk():
                print(payload.get_content_type())
                separated_mail.append({
                    'content_type': payload.get_content_type(),
                    'content':      (str)(payload.get_payload(decode=True)),
                    'is_multipart': True
                })
                print(separated_mail[1:])
                # print((str)(i) + '.' + (str)(j) + ' ' + (str)(payload.get_content_type()))
        else:
            separated_mail.append({
                'content_type': e.get_content_type(),
                'content':      (str)(e.get_payload(decode=True)),
                'is_multipart': False
            })
        separated_mails.append(separated_mail)
            # print('is not multipart!!!!!!!!!!!!!!!!!!!!!!!!')
            # print((str)
    # write_list('separated_mails', separated_mails, False)



    # mails_info = [Mails.getInfo(raw_mail) for raw_mail in raw_mails]
    # # for i, mail_info in enumerate(mails_info):
    # #     print('number: {}'.format(i))
    # #     print(mail_info)
    # # for mail in raw_mails:
    # #     for i, line in enumerate(mail):
    # #         print((str)(i) + '  ' + line)
    # mails_content = []
    # for i, (raw_mail, mail_info) in enumerate(zip(raw_mails, mails_info)):
    #     if mail_info['boundary'] != '':
    #         mail_content = Mails.separateContents(raw_mail, mail_info['boundary'])
    #         mails_content.append(mail_content)
    #         write(i, raw_mail, True)
    #         write(i, mail_info, False)
    #         write(i, mail_content, False)
    #     else:
    #         print('boundary not found: {}'.format(i))
    #         write(i, raw_mail, True)
            

def write_list(file_name, content, raw):
    if raw:
        file_name = 'log/' + (str)(file_name) + '_raw.log'
    else:
        file_name = 'log/' + (str)(file_name) + '_nrw.log'
    with open(file_name, 'w+', encoding='utf-8') as file:
        for mail in content:
            for key, value in mail[0].items():
                file.write('{}: {}\n'.format(key, value))
            file.write('----------------------------------------------------------------------------------\n')
            for content in mail[1:]:
                file.write((str)(content) + '\n')
            file.write('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


def write(file_name, content, raw):
    if raw:
        with open('log/' + (str)(file_name) + '_raw.log', 'w+', encoding='utf-8') as file:
            file.write((str)(content))
    else:
        with open('log/' + (str)(file_name) + '_nrw.log', 'w+', encoding='utf-8') as file:
            file.write((str)(content))


if __name__ == '__main__':
    __test()