import uuid
import email

from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import Login
from utils import Mails
from utils import Transfer

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

MAILS = [
    {
        'id': uuid.uuid4().hex,
        'account_id': '12345',
        'Subject': 'hello world',
        'From': 'world',
        'To': 'me',
        'Date': 'today',
        'contents': [
            {
                'content_type': 'text/html',
                'content':      '<meta charset="UTF-8"/> <table align="center" style="font-family:Microsoft YaHei,Simsun;width:700px;table-layout:fixed;" bgcolor="#ffffff"        cellpadding="0" cellspacing="0">     <tbody>     <tr>         <td style="display:none;">\\xe7\\xbd\\x91\\xe6\\x98\\x93\\xe9\\x82\\xae\\xe7\\xae\\xb1\\xe5\\xa4\\xa7\\xe5\\xb8\\x88\\xe6\\xac\\xa2\\xe8\\xbf\\x8e\\xe4\\xbf\\xa1</td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td style="width:700px;height:375px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><img                             src="https://mimg.127.net/hz/uploader/20171030/15093499095242237.jpg"                             style="display:block;border:0;"/></td>                 </tr>             </table>         </td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td rowspan="2"                         style="width:149px;height:153px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"></td>                     <td rowspan="2"                         style="width:170px;height:153px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><img                             src="https://mimg.127.net/hz/uploader/20171031/15094146237198202.jpg"                             style="display:block;border:0;"/></td>                     <td style="width:230px;height:79px;font-family:Microsoft YaHei,Simsun;background:#fcf7ff;"><a                             style="display: block;" href="http://client.dl.126.net/pcmail/dashi/8/mail.exe"                             target="_blank"><img src="https://mimg.127.net/hz/uploader/20171031/15094146239508203.jpg"                                                  style="display:block;border:0;"/></a></td>                     <td rowspan="2"                         style="width:151px;height:153px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"></td>                 </tr>                 <tr>                     <td style="width:230px;height:74px;font-family:Microsoft YaHei,Simsun;background:#fcf7ff;"><a                             style="display: block;" href="http://client.dl.126.net/macmail/dashi/mailmaster.dmg"                             target="_blank"><img src="https://mimg.127.net/hz/uploader/20171031/15094146241488204.jpg"                                                  style="display:block;border:0;"/></a></td>                 </tr>             </table>         </td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td style="width:700px;height:812px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><img                             src="https://mimg.127.net/hz/uploader/20171030/15093499106322241.jpg"                             style="display:block;border:0;"/></td>                 </tr>             </table>         </td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td style="width:700px;height:228px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><a style="display: block;"                                                                                                                    href="https://weibo.com/u/5252550107"                                                                                                                    target="_blank"><img                             src="http://mailshark.nos-jd.163yun.com/document/static/568BFCF0CC2B79A496421D588AD80CF5.png"                             style="display:block;border:0;"/></a></td>                 </tr>             </table>         </td>     </tr>     </tbody> </table>'
            }
        ],
        'read': True
    }
]

ACCOUNTS = [
    {
        'id': uuid.uuid4().hex,
        'account': '',
        'password': ''
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


def remove_account(account_id):
    for account in ACCOUNTS:
        if account['id'] == account_id:
            ACCOUNTS.remove(account)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


@app.route('/OneBox/accounts', methods=['POST', 'GET'])
def add_account():
    # print('add_account')
    response_object = {'status': 'add account success'}
    if request.method == 'POST':
        post_data = request.get_json()
        for account in ACCOUNTS:
            if account['account'] == post_data.get('account'):
                # print('account already exists')
                account['password'] = post_data.get('password')
                response_object['account_id'] = account['id']
                response_object['message'] = 'account added!'
                return jsonify(response_object)
        ACCOUNTS.append({
            'id': uuid.uuid4().hex,
            'account': post_data.get('account'),
            'password': post_data.get('password')
        })
        response_object['message'] = 'account added!'
        for account in ACCOUNTS:
            if account['account'] == post_data.get('account'):
                response_object['account_id'] = account['id']
                add_test_mails(account['id']) # for test
                break
    else:
        # not ready yet
        response_object['account'] = MAILS
    return jsonify(response_object)


@app.route('/OneBox/<account_id>', methods=['GET'])
def get_mails(account_id):
    # print('get_mails: {}'.format(account_id))
    response_object = {'status': 'get mail success'}
    account = {}
    mails = []
    for single_account in ACCOUNTS:
        if single_account['id'] == account_id:
            account = single_account
            break
    #### if there are mails of the account, clear them
    #### this step appears only removes mails on the odd position
    #### temporarily, the function cannot work properly, thus I choose to reset the MAILS every time client logins
    # for mail in MAILS:
    #     print(mail['Subject'])
    #     print(mail['account_id'])
    # for mail in MAILS:
    #     if (str)(mail['account_id']) == (str)(account_id):
    #         # print('remove duplicated mail {}'.format(mail['Subject']))
    #         MAILS.remove(mail)
    MAILS.clear()
    #### get mails of the account
    mail_link = Login.login(account, True)
    raw_mails = Mails.retrMail(mail_link, 30)
    account_mails = Mails.contentSeparator(raw_mails)
    for account_mail in account_mails:
        account_mail['id'] = uuid.uuid4().hex
        account_mail['account_id'] = account_id
        MAILS.append(account_mail)
    #### return mails
    for mail in MAILS:
        if mail['account_id'] == account_id:
            print('find mail! {}'.format(mail['Subject']))
            mails.append(mail)
    response_object['mails'] = mails
    return jsonify(response_object)


def add_test_mails(account_id):
    MAILS.append({
        'id': uuid.uuid4().hex,
        'account_id': account_id,
        'Subject': 'wobuzuorenla!!!',
        'From': '咋瓦鲁多',
        'To': '泷泽萝拉哒',
        'Date': 'today',
        'contents': 'hello world',
        'read': True
    })


if __name__ == '__main__':
    app.run()