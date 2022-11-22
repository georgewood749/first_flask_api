from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest

app = Flask(__name__)
CORS(app)


doggos = [
    {'id': 1, 'name': 'Fido', 'age': 9},
    {'id': 2, 'name': 'Scoob', 'age': 2},
    {'id': 3, 'name': 'Milo', 'age': 12}
]
