import requests
from flask import Flask
app = Flask(__name__)


@app.route('/url')
def get_data():
    return requests.get('https://jsonplaceholder.typicode.com/users').content
