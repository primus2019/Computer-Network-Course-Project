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
        'content': 'hello world',
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
    # for mail in MAILS:
    #     print(mail['Subject'])
    #     print(mail['account_id'])
    for mail in MAILS:
        if (str)(mail['account_id']) == (str)(account_id):
            # print('remove duplicated mail {}'.format(mail['Subject']))
            MAILS.remove(mail)
    #### get mails of the account
    mail_link = Login.login(account, True)
    raw_mails = Mails.retrMail(mail_link, 10)
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