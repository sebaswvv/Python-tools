from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import TodoDto
from ..service.todo_service import save_new_todo
from typing import Dict, Tuple

api = TodoDto.api

# create new todo only if user is logged in
@api.route('/')
class TodoList(Resource):
    @api.expect(TodoDto.todo, validate=True)
    @api.response(201, 'Todo successfully created.')
    @api.doc('create a new todo')
    @token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Todo """
        data = request.json
        print(data)
        # return save_new_todo(data=data)


# @api.route('/')
# class UserList(Resource):
#     @api.doc('list_of_registered_users')
#     @admin_token_required
#     @api.marshal_list_with(_user, envelope='data')
#     def get(self):
#         """List all registered users"""
#         return get_all_users()

#     @api.expect(_user, validate=True)
#     @api.response(201, 'User successfully created.')
#     @api.doc('create a new user')
#     def post(self) -> Tuple[Dict[str, str], int]:
#         """Creates a new User """
#         data = request.json
#         return save_new_user(data=data)


# @api.route('/<public_id>')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(_user)
#     def get(self, public_id):
#         """get a user given its identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             return user
        
# @api.route('/<public_id>/todos')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class UserTodos(Resource):
#     @api.doc('get a user todos')
#     @api.marshal_with(_user)
#     def get(self, public_id):
#         """get a user todos given its identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             return user.todos


