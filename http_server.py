import flask
from flask import Flask
from flask import render_template
from e_socket import ESocket
from e_socket import SOCKET_MAP
import config

app = Flask(__name__)
e_sockets = {}


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/socket/<name>',  methods=['GET', 'POST'])
def update_socket(name):
    if flask.request.method == 'GET':
        e_sockets[name].toggle()
    elif flask.request.method == 'POST':
        data = flask.request.json
        if data['State'] == "on":
            e_sockets[name].turn_on()
        elif data['State'] == "off":
            e_sockets[name].turn_off()
        else:
            print("Invalid state: %s" % data)
    return ''


def start():
    for key in SOCKET_MAP:
        e_sockets[key] = ESocket(key)
    app.run(host='0.0.0.0', port=config.HTTP_PORT)


if __name__ == '__main__':
    start()
