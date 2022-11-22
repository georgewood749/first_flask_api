from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest

# from models import Doggo
# import db


app = Flask(__name__)
CORS(app)


doggos = [
    {'id': 1, 'name': 'Fido', 'age': 9},
    {'id': 2, 'name': 'Scoob', 'age': 2},
    {'id': 3, 'name': 'Milo', 'age': 12}
]

def find_by_id(id):
    try:
        return next(doggo for doggo in doggos if doggo['id'] == id)
    except:
        raise BadRequest(f"We don't have that doggo with id {id}!")


@app.route("/")
def hello_world():
    return f"Hello world!"


@app.route("/doggos", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(doggos), 200


def create():
    if request.method == "POST":
        data = request.json
        last_id = doggos[-1]["id"]
        data["id"] = last_id + 1
        doggos.append(data)
        print(data)
        return f"{data['name']} was added to the database.", 201


@app.route("/doggos/<int:doggo_id>", methods=["GET", "PATCH", "DELETE"])
def show(doggo_id):
    if request.method == "GET":
        try:
            return next(dog for dog in doggos if dog['id'] == doggo_id), 302
        except:
            raise BadRequest(f"Could not find this doggo in the database.")


def destroy(doggo_id):
    if request.method == "DELETE":
        try:
            doggo = find_by_id(doggo_id)
            doggos.remove(doggo)
            return f"Doggo {doggo['name']} was removed from the database", 204
        except:
            raise BadRequest(f"Could not find this doggo in the database.")


def update(doggo_id):
    if request.method == "PATCH":
        try:
            pass
        except:
            pass


@app.errorhandler(NotFound)
def handle_404(err):
    return jsonify({"message": f"Doggo not found. {err}"}), 404


@app.errorhandler(InternalServerError)
def handle_500(err):
    return jsonify({"message": f"Internal server error"}), 500


if __name__ == "__main__":
    app.run()
