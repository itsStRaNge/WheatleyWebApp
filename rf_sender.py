from flask import Flask
from flask import render_template
from flask import request
from flask import abort


HOST = '0.0.0.0'  # all interfaces
PORT = 8080

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/socket/<nr>',  methods=['GET'])
def update_socket(nr):
    print(nr)
    return ''


if __name__ == '__main__':
    # start http server
    app.run(host=HOST, port=PORT)
