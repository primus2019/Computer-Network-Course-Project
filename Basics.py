import re
import Transfer


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
    print([Transfer.encode(info) for info in basic_info.values()])
    return basic_info

    
    
# (?:to:\s*[\'\"]*(<to>[^\'\";]*)[\'\";]*)?(?:subject:\s*[\'\"]*(<subject>[^\'\";]*)[\'\";]*)?(?:date:\s*[\'\"]*(<date>[^\'\";]*)[\'\";]*)?(?:cc:\s*[\'\"]*(<cc>[^\'\";]*)[\'\";]*)?(?:boundary=\s*[\'\"]*(<boundary>[^\'\";]*)