import smtplib
import email

from os.path import basename, abspath, join
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.message import MIMEMessage

from utils import Login


def __test():
    mail_host = 'smtp.163.com'
    vertification = {
        'account':  'primus1998@163.com',
        'password': 'jlc123456'
    }

    send_mail(
        vertification=vertification,
        mail={
            # 'Subject': 'my homework for dynamic system',
            # 'To': 'jilincheng<jilincheng1998@163.com>; primus<primus1998@163.com>',
            # 'contents': [
            #     {
            #         'content_type': 'text/plain',
            #         'content': 'Dear manager: the enclosed is my application, please check it.'
            #     },
            #     {
            #         'content_type': 'multipart/application',
            #         'content': r'C:\Primus\Codes\Python\CN\Computer-Network-Course-Project\server\tmp\b.zip'
            #     },
            #     {
            #         'content_type': 'multipart/application',
            #         'content': r'C:\Primus\Codes\Python\CN\Computer-Network-Course-Project\server\tmp\a.py'
            #     }
            # ]
        }
    )


def send_mail(vertification, mail, account_id='', reply_mail_id=''):
    mail_host = 'smtp.163.com'

    # preprocessing
    mail['To'] = mail['To'].replace(' ', '').split(';')
    mail.update({
        'contents': 
            [
                {
                    'content_type': 'text/plain',
                    'content': mail['Text']
                }
            ]
    })
    if mail['Application'] is not None and mail['Application'] != '':
        mail['contents'].append({
            'content_type': 'multipart/application',
            'content': mail['Application']
        })
    
    # prepare reply mail
    if account_id != '' and reply_mail_id != '':
        origin_mail = email.message_from_string(open('mails/{}/{}.log'.format(account_id, reply_mail_id), 'r', encoding='utf-8').read())
        for part in origin_mail.walk():
            if (part.get('Content-Disposition') and part.get('Content-Disposition').startswith("attachment")):
                part.set_type("text/plain")
                part.set_payload("Attachment removed: %s (%s, %d bytes)"
                                %(part.get_filename(), 
                                part.get_content_type(), 
                                len(part.get_payload(decode=True))))
                del part["Content-Disposition"]
                del part["Content-Transfer-Encoding"]

    # for test
    Login.log('mail: {}'.format((str)(mail)))

    multipart = MIMEMultipart('mixed')
    multipart['Subject'] = mail['Subject']
    multipart['From'] = vertification['account']
    for content in mail['contents']:
        if content['content_type'] == 'text/plain':
            multipart.attach(MIMEText(content['content'], 'plain', 'utf-8'))
        elif content['content_type'] == 'multipart/application':
            Login.log('find absolute path for attachment: ' + join(abspath("attachments\\"), content['content']))
            attachment = MIMEApplication(open(join(abspath("attachments\\"), content['content']), 'rb').read(), Name=content['content'])
            attachment['Content-Disposition'] = 'attachment; filename={}'.format(content['content'])
            multipart.attach(attachment)
            # multipart.attach(MIMEApplication(content['content']))
        else:
            Login.log('error in content_type: {}'.format(content['content_type']))
    if account_id != '' and reply_mail_id != '':
        multipart["Message-ID"] = email.utils.make_msgid()
        multipart["In-Reply-To"] = origin_mail["Message-ID"]
        multipart["References"] = origin_mail["Message-ID"]
        multipart['Subject'] = 'Re: {}'.format(origin_mail['Subject'])
        multipart.attach(MIMEMessage(origin_mail))
    try:
        smtp = smtplib.SMTP_SSL(mail_host, 465)
        smtp.login(vertification['account'], vertification['password'])
        smtp.sendmail(vertification['account'], mail['To'], multipart.as_string())
    except Exception as e:
        Login.log((str)(e))
    


if __name__ == '__main__':
    __test()