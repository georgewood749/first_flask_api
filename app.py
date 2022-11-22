from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest


app = Flask(__name__)
CORS(app)


doggos = [
    {'id': 1, 'name': 'Fido', 'age': 9},
    {'id': 2, 'name': 'Scoob', 'age': 2},
    {'id': 3, 'name': 'Milo', 'age': 12}
]


@app.route("/")
def hello_world():
    return f"Hello world!"


@app.route("/doggos", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(doggos)
    elif request.method == "POST":
        data = request.json
        last_id = doggos[-1]["id"]
        data["id"] = last_id + 1
        doggos.append(data)
        print(data)
        return f"{data['name']} was added to the database.", 201


@app.route("/doggos/<int:doggo_id>")
def show(doggo_id):
    try:
        return next(dog for dog in doggos if dog['id'] == doggo_id), 302
    except:
        raise BadRequest(f"Could not find this doggo in the database.")


@app.errorhandler(NotFound)
def handle_404(err):
    return jsonify({"message": f"Doggo not found. {err}"}), 404


@app.errorhandler(InternalServerError)
def handle_500(err):
    return jsonify({"message": f"Internal server error"}), 500


if __name__ == "__main__":
    app.run()
