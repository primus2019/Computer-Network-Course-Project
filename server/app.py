import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


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
        'subject': 'hello world',
        'sender': 'world',
        'receiver': 'me',
        'date': 'today',
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
    response_object = {'status': 'add account success'}
    if request.method == 'POST':
        post_data = request.get_json()
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
    response_object = {'status': 'get mail success'}
    mails = []
    for mail in MAILS:
        if mail['account_id'] == account_id:
            mails.append(mail)
    response_object['mails'] = mails
    return jsonify(response_object)


def add_test_mails(account_id):
    MAILS.append({
        'id': uuid.uuid4().hex,
        'account_id': account_id,
        'subject': 'wobuzuorenla!!!',
        'sender': '咋瓦鲁多',
        'receiver': '泷泽萝拉哒',
        'date': 'today',
        'content': 'hello world',
        'read': True
    })


if __name__ == '__main__':
    app.run()