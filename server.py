from flask import Flask, jsonify


app = Flask('app')


def hello_world():
    response = jsonify({'Hello': 'world'})
    print(response)
    return response


app.add_url_rule('/hello/world', view_func=hello_world, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)