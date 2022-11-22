from werkzeug.exceptions import BadRequest


doggos = [
    {'id': 1, 'name': 'Fido', 'age': 9},
    {'id': 2, 'name': 'Scoob', 'age': 2},
    {'id': 3, 'name': 'Milo', 'age': 12}
]

def index(req):
    return [c for c in doggos], 200

def show(req, id):
    return find_by_id(id), 200

def create(req):
    new_doggo = req.get_json()
    new_doggo['id'] = sorted([c['id'] for c in doggos])[-1] + 1
    doggos.append(new_doggo)
    return new_doggo, 201

def update(req, id):
    doggo = find_by_id(id)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        doggo[key] = val
    return doggo, 200

def destroy(req, id):
    doggo = find_by_id(id)
    doggos.remove(doggo)
    return doggo, 204

def find_by_id(id):
    try:
        return next(doggo for doggo in doggos if doggo['id'] == id)
    except:
        raise BadRequest(f"We don't have that doggo with id {id}!")