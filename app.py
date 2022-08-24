from crypt import methods
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods= ['GET'])
def home():
    return "<h1> WELCOME, YOU CAN SEND INFORMATION BY FILLING OUT THIS FORM</h1><p>This site is a prototyp API for interacting with channel on discord by using bots</p>"

