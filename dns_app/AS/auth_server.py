from flask import Flask, Response, requests
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def handle_registration():
    return

@app.route('/')
def handle_query():
    args = requests.args
    return()

app.run(host='0.0.0.2',
        port=53533,
        debug=True)
