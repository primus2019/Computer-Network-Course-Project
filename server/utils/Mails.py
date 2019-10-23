import re
import email
import base64

from email.parser import HeaderParser
from utils import Transfer


def retrMail(mailLink, retr_num=0):
    '''retr existing mails in the logged mailbox
    '''
    # clearLog()
    try:
        # only 1# element is useful; see mail_info.log
        mail_list = [[(int)(mail_idx), (int)(mail_myth)] for mail_idx, mail_myth in (item.decode('utf-8').split(' ') for item in mailLink.list()[1])]
        # clearLog()
        if retr_num == 0:
            retr_num = mail_list[-1][0]
        if len(mail_list) == 0:
            return None
        # number = mail_info[0]
        # mail = mailLink.retr(number)[1]
        raw_mail_info = []
        for i in range(1, retr_num):
            mail_info = [info.decode('utf-8') for info in mailLink.retr(i)[1:][0]]
            raw_mail_info.append(mail_info)
            
            # for info in mailLink.retr(i)[1:][0]:
            #     # print('##############################' + info.decode('utf-8'))
            #     mail_info.append(info.decode('utf-8'))
            
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
        return raw_mail_info
    except Exception as e:
        print(str(e))
        return None


def getInfo(mail_info):
    '''Get basic information of given SINGLE mail
    '''
    basic_info = {'from': '', 'to': '', 'subject': '', 'date': '', 'cc': '', 'boundary': ''}
    list = []
    for line in mail_info:
        obj_cc              = re.search(r'(?:cc:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',     line, flags=re.IGNORECASE)
        obj_subject         = re.search(r'(?:subject:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',line, flags=re.IGNORECASE)
        obj_to              = re.search(r'(?:to:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',     line, flags=re.IGNORECASE)
        obj_from            = re.search(r'(?:from:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',   line, flags=re.IGNORECASE)
        obj_date            = re.search(r'(?:date:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',   line, flags=re.IGNORECASE)
        obj_content_type    = re.search(r'(?:content-type:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*(?:format:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*', line, flags=re.IGNORECASE)
        obj_charset         = re.search(r'(?:charset:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*',line, flags=re.IGNORECASE)
        obj_transfer_encoding = re.search(r'(?:content-transfer-encoding:\s*[\'\"]*([^\'\";]*)[\'\";]*)?[\s]*', line, flags=re.IGNORECASE)
        obj_boundary        = re.search(r'(?:boundary=\s*[\'\"]*([^\'\";]*)[\'\";]*)', line, flags=re.IGNORECASE)
        if obj_from.group(1)    is not None:
            basic_info['from']     = obj_from.group(1)
        if obj_to.group(1)      is not None:
            basic_info['to']       = obj_to.group(1)
        if obj_subject.group(1) is not None:
            basic_info['subject']  = obj_subject.group(1)
        if obj_date.group(1)    is not None:
            basic_info['date']     = obj_date.group(1)
        if obj_cc.group(1)      is not None:
            basic_info['cc']       = obj_cc.group(1)
        if obj_boundary         is not None:
            basic_info['boundary'] = obj_boundary.group(1)
    return {key: Transfer.encode(basic_info[key]) for key in basic_info}
    # print([Transfer.encode(info) for info in basic_info.values()])
    # return ([Transfer.encode(info) for info in basic_info.values()])


def separateContents(raw_mail, boundary):
    '''Separate mail by boundary, and extract content type
    '''
    mail_content = []
    pattern = '(?=' + boundary + '([\s\S]*?)' + boundary + ')'
    raw_mail = '\n'.join(raw_mail)
    contents =  re.findall(pattern, raw_mail, flags=re.IGNORECASE|re.MULTILINE)
    # contents may look like ['ssssss', 'aaaaaa']
    for content in contents[1:]:
        tmp = {
            'content_type': '',
            'content_transfer_encoding': '',
            'content': ''
        }
        content_type = re.findall(r'Content-Type:\s(.*?)[;\n]', content, flags=re.IGNORECASE|re.MULTILINE)
        content_transfer_encoding = re.findall(r'Content-Transfer-Encoding:\s(.*?)[;\n]', content, flags=re.IGNORECASE|re.MULTILINE)
        rest_content = re.findall(r'\n\n([\s\S]*)', content, flags=re.IGNORECASE|re.MULTILINE)
        if content_type is not None:
            tmp['content_type'] = content_type
        if content_transfer_encoding is not None:
            tmp['content_transfer_encoding'] = content_transfer_encoding
        if rest_content is not None:
            tmp['content'] = rest_content
        mail_content.append(tmp)
    return mail_content


def contentSeparator(raw_mails):
    '''enter lists of raw mails and returns list of list of jsons of mail content
    like [[{json of a content}, {json of a content}, ...], [another mail], ...]
    '''
    separated_mails = []
    assert raw_mails is not None, 'received nothing from mail box'
    for i, raw_mail in enumerate(raw_mails): # raw_mail must be string
        separated_mail = {'contents': []}
        raw_mail = '\n'.join(raw_mail)

        header_info = email.parser.HeaderParser().parsestr(raw_mail)
        separated_mail.update({
            key: Transfer.encode(value) for key, value in header_info.items()
        })
        
        e = email.message_from_string(raw_mail)
        if e.is_multipart():
            # print('is multipart!')
            for payload in e.walk():
                # print(payload.get_content_type())
                # tmp = ''
                # if payload.get_payload(decode=True) is not None:
                #     tmp = payload.get_payload(decode=True).decode('utf-8')
                separated_mail['contents'].append({
                            'content_type': payload.get_content_type(),
                            'content':      payload.get_payload(decode=True),
                            # 'content':      tmp,
                            'content_charset': payload.get_content_charset(),
                            'is_multipart': True
                        
                })
                # print(separated_mail[1:])
        else:
            separated_mail['contents'].append({
                'content_type': e.get_content_type(),
                'content':      (str)(e.get_payload(decode=True)),
                'content_charset': e.get_content_charset(),
                'is_multipart': False
            })
        print('dealing with mail {}'.format(i))
        __write_mail_contents(separated_mail, i)
        separated_mail = deal_with_nonetype(separated_mail)
        separated_mail = deal_with_content(separated_mail)
        separated_mail = deal_with_nonetype(separated_mail)
        separated_mail = deal_with_newline(separated_mail)
        separated_mails.append(separated_mail)
    return separated_mails


def deal_with_nonetype(separated_mail):
    tmp = []
    for mail_content in separated_mail['contents']:
        if mail_content['content'] is not None and mail_content['content'] != 'None':
            tmp.append(mail_content)
    separated_mail['contents'] = tmp
    return separated_mail


def deal_with_newline(separated_mail):
    for mail_content in separated_mail['contents']:
        if mail_content['content_type'] == 'text/plain':
            mail_content['content'] = mail_content['content'].replace(r'\n', '</br>')
        elif mail_content['content_type'] == 'text/html':
            mail_content['content'] = mail_content['content'].replace(r'\n', '')
        else:
            mail_content['content'] = mail_content['content'].replace(r'\n', '</br>')
    return separated_mail


def deal_with_content(separated_mail):
    for mail_content in separated_mail['contents']:
        if type(mail_content['content']) == str:
            continue
        if mail_content['content_charset'] == 'utf-8':
            mail_content['content'] = str(mail_content['content'], 'utf-8', 'ignore')# .decode('utf-8')
        elif mail_content['content_charset'] == 'gbk':
            mail_content['content'] = str(mail_content['content'], 'gbk', 'ignore')# .decode('gbk')
        elif mail_content['content_charset'] == 'gb18030':
            mail_content['content'] = str(mail_content['content'], 'gb18030', 'ignore')# .decode('gbk')
        else:
            print('new content_charset: {}'.format(mail_content['content_charset']))
            mail_content['content'] = str(mail_content['content'], mail_content['content_charset'], 'ignore')# .decode('gbk')
    return separated_mail



def __write_mail_contents(separated_mail, i):
    with open('log/{}.log'.format(i), 'w+') as file:
        for content in separated_mail['contents']:
            file.write('content_type: {}\n'.format(content['content_type']))
            file.write('content: {}\n'.format(content['content']))
            file.write('content_charset: {}\n'.format(content['content_charset']))
            file.write('++++++++++++++++++++++++++++++++++++++++++++++++\n')

