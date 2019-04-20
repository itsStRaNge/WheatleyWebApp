from flask import Flask
from flask import render_template
from e_socket import ESocket
from e_socket import SOCKET_MAP


HOST = '0.0.0.0'  # all interfaces
PORT = 8080

app = Flask(__name__)

e_sockets = {}


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/socket/<name>',  methods=['GET'])
def update_socket(name):
    e_sockets[name].toggle()
    return ''


def start():
    for key in SOCKET_MAP:
        e_sockets[key] = ESocket(key)
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    start()
