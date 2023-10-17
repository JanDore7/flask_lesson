from typing import Type
from sqlalchemy.exc import IntegrityError
import pydantic
from flask import Flask, jsonify, request
from models import Session, User
from flask.views import MethodView
from schema import CreateUser, UpdateUser


app = Flask('app')


class HttpError(Exception):

    def __init__(self, status_code: int, message: str | dict| list):
        self.status_code = status_code
        self.message = message


@app.errorhandler(HttpError)
def error_handler(er: HttpError):
    if isinstance(er.message, pydantic.ValidationError):
        error_list = []
        for error in er.message.errors():
            error_list.append({'type': 'value_error', 'loc': error['loc'], 'msg': error['msg'], 'input': error['input']})
        response = jsonify({'status': 'Ошибка', 'errors': error_list})
    else:
        response = jsonify({'status': 'error', 'message': str(er.message)})  # Convert the error message to a string
    response.status_code = er.status_code
    return response


def validate(validation_schema: Type[CreateUser] | Type[UpdateUser], json_data):
    try:
        pydantic_object = validation_schema(**json_data)
        return pydantic_object.model_dump(exclude_none=True)

    except pydantic.ValidationError as er:
        raise HttpError(400, er.errors())


class UserViews(MethodView):

    def get(self):
        pass

    def post(self):
        validate_data = validate(CreateUser, request.json)
        with Session() as session:
            new_user = User(**validate_data)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError as er:
                raise HttpError(409, 'Such a user already exists')
            return jsonify({'id': new_user.id})

    def patch(self):
        pass

    def delete(self):
        pass


user_view = UserViews.as_view('users')

app.add_url_rule('/user/<int:user_id>', view_func=user_view, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/user', view_func=user_view, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)