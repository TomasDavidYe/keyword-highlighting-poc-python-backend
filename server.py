from flask import Flask, send_file, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get-javascript')
def get_javascript_file():
    return send_file('highlight-script.js', attachment_filename='highlight-script.js')


@app.route('/get-keywords-for-text')
def get_keywords():
    result = {}
    body = request.args.get('body')
    keyword_dict = get_keyword_dict()
    keys = set(keyword_dict.keys())

    for word in body.split():
        if word in keys:
            result[word] = keyword_dict[word]

    json_result = json.dumps(result, indent=2)
    print(json_result)

    return json_result


def get_keyword_dict():
    return {
        "invest": {
            "keyword": "invest",
            "link": "https://en.wikipedia.org/wiki/Investment"
        },
        "interest": {
            "keyword": "interest",
            "link": "https://en.wikipedia.org/wiki/Interest"
        },
        "401k": {
            "keyword": "401k",
            "link": "https://en.wikipedia.org/wiki/401(k)"
        }
    }
