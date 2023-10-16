from flask import Flask, jsonify, request


app = Flask('app')


def hello_world(some_id):

    json_data = request.json
    handler = request.headers
    qs = request.args
    print(f'{json_data=}, {handler=}, {qs=}')

    response = jsonify({'Hello': 'world'})
    print(response)
    return response


app.add_url_rule('/hello/world/<int:some_id>', view_func=hello_world, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)