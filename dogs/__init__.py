from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest

from .routes.main import main_routes

#db stuff
from dotenv import load_dotenv
from os import environ
from .database.db import db

load_dotenv()
database_uri = environ.get('DATABASE_URL')

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)


with app.app_context():
    db.app = app
    db.init_app(app)

@app.route("/")
def hello_world ():
    return f"Hello, World of Doggos!"

app.register_blueprint(main_routes)

@app.errorhandler(NotFound)
def handle_404 (err):
    return jsonify({"message": f"No doggos in sight {err}"}), 404

@app.errorhandler(InternalServerError)
def handle_500(err):
    return jsonify({"message": f"It's not you, it's me!"}), 500

if __name__ == "__main__":
    app.run(debug=True)
