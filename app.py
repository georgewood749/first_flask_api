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
def hello_world ():
    return f"Hello, World of Doggos!"

@app.route("/dogs", methods=["GET", "POST"])
def index ():
    if request.method == "GET":
        return jsonify(doggos)
    elif request.method == "POST":
        data = request.json
        last_id = doggos[-1]["id"]
        data["id"] = last_id + 1
        doggos.append(data)
        print(data)
        return f"{data['name']} was added to Doggos", 201

@app.route("/dogs/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show (id):
        # GET
        if request.method == "GET":
            try:
                return next(dogs for dogs in doggos if dogs['id'] == id), 302
            except:
                raise BadRequest(f"Doggo not found")

        # Patch
        elif request.method  == "PATCH":
            try:
                data = request.json
                for dog in doggos:
                    if dog['id'] == id:
                        for key, val in data.items():
                            dog[key] = val
                return f"{data['name']} was updated in Doggos", 200
            except:
                raise BadRequest(f"Doggo not found")

        # Delete
        elif request.method == "DELETE":
            try:
                for dog in doggos:
                    if dog['id'] == id:
                        doggos.remove(dog)
                return f"{data['name']} was removed from Doggos", 204    
            except:
                raise BadRequest(f"Doggo not found")
     

@app.errorhandler(NotFound)
def handle_404 (err):
    return jsonify({"message": f"No doggos in sight {err}"}), 404

@app.errorhandler(InternalServerError)
def handle_500(err):
    return jsonify({"message": f"It's not you, it's me!"}), 500

if __name__ == "__main__":
    app.run()
