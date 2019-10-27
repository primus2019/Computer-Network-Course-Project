import quopri
import base64
import re


def encode(raw):
    # check out the enhancing charset and encoding
    # encoding: quoted-printable; base64/base32
    # charset: utf-8; gbk
    # print(raw)
    formats = re.search(r'=\?(.*)\?(.)\?(.*)\?=(.*)', raw, flags=re.IGNORECASE)
    if formats is None:
        return raw
    if formats.group(1).lower() == 'utf-8' or formats.group(1).lower() == 'utf8':
        if formats.group(2).lower() == 'q':
            return quopri.decodestring(formats.group(3)).decode('utf-8', errors='ignore') + formats.group(4)
        if formats.group(2).lower() == 'b':
            return base64.b64decode(formats.group(3)).decode('utf-8', errors='ignore') + formats.group(4)
        else:
            print('exception!!')
            return None
    elif formats.group(1).lower() == 'gbk':
        if formats.group(2).lower() == 'q':
            return quopri.decodestring(formats.group(3)).decode('gbk', errors='ignore') + formats.group(4)
        if formats.group(2).lower() == 'b':
            return base64.b64decode(formats.group(3)).decode('gbk', errors='ignore') + formats.group(4)
        else:
            print('exception!!')
            return None
    # if gb2312
    elif formats.group(1).lower() == 'gb2312':
        if formats.group(2).lower() == 'q':
            return quopri.decodestring(formats.group(3)).decode('gb2312', errors='ignore') + formats.group(4)
        if formats.group(2).lower() == 'b':
            return base64.b64decode(formats.group(3)).decode('gb2312', errors='ignore') + formats.group(4)
    # if us-ascii
    elif formats.group(1).lower() == 'us-ascii':
        if formats.group(2).lower() == 'q':
            return quopri.decodestring(formats.group(3)).decode('us-ascii', errors='ignore') + formats.group(4)
        if formats.group(2).lower() == 'b':
            return base64.b64decode(formats.group(3)).decode('us-ascii', errors='ignore') + formats.group(4)
    else:
        print('exception!!!!{}'.format(formats.group(1).lower()))
        return None
    return None


