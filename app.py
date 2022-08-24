from crypt import methods
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


information = [
    {"chanel_one": "This is message for chanel one"},
    {"chanel_two": "This is message for chanel two"}
]


@app.route('/', methods= ['GET'])
def home():
    return "<h1> WELCOME, YOU CAN SEND INFORMATION BY FILLING OUT THIS FORM</h1><p>This site is a prototyp API for interacting with channel on discord by using bots</p>"

@app.route('/api/v1/test_endpoint', methods= ['GET'])
def api():
    return jsonify(information)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404