import os
import uuid
import email

from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import Login
from utils import Mails
from utils import Transfer
from utils import Sender

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
        'contents': [],
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
    Login.clearLog()
    Login.clearCache()
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
        account_id = uuid.uuid4().hex
        ACCOUNTS.append({
            'id': account_id,
            'account': post_data.get('account'),
            'password': post_data.get('password')
        })
        response_object['message'] = 'account added!'
        response_object['account_id'] = account_id
        if not os.path.isdir('tmp/'):
            os.mkdir('tmp/')
        if not os.path.isdir('mails/'):
            os.mkdir('mails/')
        if not os.path.isdir('tmp/{}/'.format(account_id)):
            os.mkdir('tmp/{}/'.format(account_id))
        if not os.path.isdir('mails/{}/'.format(account_id)):
            os.mkdir('mails/{}/'.format(account_id))
    else:
        # not ready yet
        response_object['account'] = MAILS
    return jsonify(response_object)


@app.route('/OneBox/<account_id>', methods=['POST', 'GET'])
def send_mail(account_id):
    if request.method == 'POST':
        response_object = {'status': 'send mail success'}
        Login.log('sending mail...')
        vertification = {}
        # find vertification of the account
        for account in ACCOUNTS:
            if account['id'] == account_id:
                vertification = account
                Login.log('find account: {}'.format((str)(vertification)))
                break
        # the posted data is in form of jsonified mail as sent to client, so do the reverse
        post_data = request.get_json()
        Sender.send_mail(vertification, post_data)
        Login.log('Mail sent!')
        response_object.update({'message': 'Mail sent!'})
        return jsonify(response_object)
    else: # GET, when getting mails
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
        # raw_mails = Mails.retrMail(mail_link, end_retr_num=60, start_retr_num=10)
        # retrieve all the mails
        raw_mails = Mails.retrMail(mail_link)
        account_mails = Mails.contentSeparator(account_id, raw_mails)
        for raw_mail, account_mail in zip(raw_mails, account_mails):
            mail_id = uuid.uuid4().hex
            Mails.__save_raw_mails(raw_mail, account_id, mail_id)
            account_mail['id'] = mail_id
            account_mail['account_id'] = account_id
            MAILS.append(account_mail)
        #### return mails
        #### NOTICE: the function is designed to dynamically send mail to client at 100 a time
        #### and in reverse
        for mail in MAILS:
            if mail['account_id'] == account_id:
                if 'Subject' in mail.keys():
                    Login.log('find mail! {}'.format(mail['Subject']))
                else:
                    Login.log('find mail without Subject!\n{}'.format((str)(mail)))
                mails.append(mail)
        mails.reverse()
        response_object['mails'] = mails
        return jsonify(response_object)


@app.route('/OneBox/<account_id>/<mail_id>', methods=['POST'])
def reply_mail(account_id, mail_id):
    if request.method == 'POST':
        response_object = {'status': 'reply mail success'}
        Login.log('replying mail...')
        vertification = {}
        # find vertification of the account
        for account in ACCOUNTS:
            if account['id'] == account_id:
                vertification = account
                Login.log('find account: {}'.format((str)(vertification)))
                break
        # the posted data is in form of jsonified mail as sent to client, so do the reverse
        post_data = request.get_json()
        Sender.send_mail(vertification, post_data, account_id, mail_id)
        Login.log('Mail replied!')
        response_object.update({'message': 'Mail replied!'})
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
    # Login.clearLog()
    app.run()