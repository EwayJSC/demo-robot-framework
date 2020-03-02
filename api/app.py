from random import randint

from flask import Flask

app = Flask(__name__)
storage = {}


@app.route('/users/<string:name>/number', methods=["GET"])
def get_current_number(name):
    return str(storage.get(name, 0))


@app.route('/users/<string:name>/number', methods=["POST"])
def new_number(name):
    storage[name] = randint(1, 100000)
    return str(storage.get(name))


if __name__ == '__main__':
    app.run("0.0.0.0", port=8080)
