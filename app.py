from flask import Flask, request, jsonify
import Logging

logger = logging. getLogger()
Logger.setLevel (Logging.INFO)

app = Flask(__name_)

@app.route("/")

def hello_wortd():
    return “Hello world"

if _name_ == '_main_':
    app.run(port=8080, host="0.0.0.0"
