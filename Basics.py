import re


def getInfo(mail_info):
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
        if obj_from.group(1) is not None:
            basic_info['from'] = obj_from.group(1)
        if obj_to.group(1) is not None:
            print('to: '                        + obj_to.group(1))
        if obj_date.group(1) is not None:
            print('date: '                      + obj_date.group(1))
        if obj_cc.group(1) is not None:
            print('cc: '                        + obj_cc.group(1))
        if obj_content_type.group(1) is not None:
            print('content-type: '              + obj_content_type.group(1))
        if obj_charset.group(1) is not None:
            print('charset: '                   + obj_charset.group(1))
        if obj_transfer_encoding.group(1) is not None:
            print('content-transfer-encoding: ' + obj_transfer_encoding.group(1))
        if obj_boundary is not None:
            print('boundary: '                    + obj_boundary.group(1))
    
    
# (?:to:\s*[\'\"]*(<to>[^\'\";]*)[\'\";]*)?(?:subject:\s*[\'\"]*(<subject>[^\'\";]*)[\'\";]*)?(?:date:\s*[\'\"]*(<date>[^\'\";]*)[\'\";]*)?(?:cc:\s*[\'\"]*(<cc>[^\'\";]*)[\'\";]*)?(?:boundary=\s*[\'\"]*(<boundary>[^\'\";]*)