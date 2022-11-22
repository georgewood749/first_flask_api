from flask import Blueprint, request, jsonify
from werkzeug import exceptions
from ..database.db import db
from ..models.doggos import Doggo

main_routes = Blueprint('main', __name__)

@main_routes.route("/dogs", methods=["GET", "POST"])
def index ():
    if request.method == "GET":
        doggos = Doggo.query.all()
        outputs = map(lambda p: {'name': p.name, 'age': p.age}, doggos)
        useable_outputs = list(outputs)
        return jsonify(useable_outputs), 200
    elif request.method == "POST":
        data = request.json
        # last_id = doggos[-1]["id"]
        # data["id"] = last_id + 1
        new_doggo = Doggo(name=data['name'], age=data['age'])
        db.session.add(new_doggo)
        db.session.commit()
        # doggos.append(data)
        # print(data)
        return jsonify(data), 201

@main_routes.route("/dogs/<string:name>", methods=["GET", "PATCH", "DELETE"])
def show (dog_name):
        # GET
        if request.method == "GET":
            try:
                foundDog = Doggo.query.filter_by(name=str(dog_name)).first()
                output = {'name': foundDog.name, 'age': foundDog.age}
                return output
            except:
                raise exceptions.BadRequest(f"Doggo not found")

        # # Patch
        # elif request.method  == "PATCH":
        #     try:
        #         # data = request.json
        #         # for dog in doggos:
        #         #     if dog['id'] == id:
        #         #         for key, val in data.items():
        #         #             dog[key] = val
        #         # return f"{data['name']} was updated in Doggos", 200
        #     except:
        #         raise exceptions.BadRequest(f"Doggo not found")

        # Delete
        elif request.method == "DELETE":
            try:
                foundDog = Doggo.query.filter_by(name=str(dog_name))
                db.session.delete(foundDog)
                db.session.commit()
                return f"removed from Doggos", 204    
            except:
                raise exceptions.BadRequest(f"Doggo not found")
