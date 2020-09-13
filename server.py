from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get-javascript')
def get_javascript_file():
    return send_file('highlight-script.js', attachment_filename='highlight-script.js')
