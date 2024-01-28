import uuid
import datetime

from app.main import db
from app.main.model.todo import Todo
from typing import Dict, Tuple

def save_new_todo(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    todo = Todo.query.filter_by(name=data['name']).first()
    if not todo:
        new_todo = Todo(
            name=data['name'],
            description=data['description'],
            user_id=data['user_id']
        )
        save_changes(new_todo)
        response_object = {
            'status': 'success',
            'message': 'Successfully created todo.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Todo already exists.',
        }
        return response_object, 409


def save_changes(data: Todo) -> None:
    db.session.add(data)
    db.session.commit()

