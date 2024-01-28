from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class TodoDto:
    api = Namespace('todo', description='todo related operations')
    todo = api.model('todo', {
        'content': fields.String(required=True, description='todo content'),
        'completed': fields.Boolean(required=False, description='todo completed'),
        'user_id': fields.Integer(required=True, description='todo user id')
    })