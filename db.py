import sqlite3
import random
import datetime
from models import Doggo


def getNewId():
    return random.getrandbits(28)


doggos = [
    {
        "age": 9,
        "id": 1,
        "name": "Fido"
    },
    {
        "age": 2,
        "id": 2,
        "name": "Scoob"
    },
    {
        "age": 12,
        "id": 3,
        "name": "Milo"
    },
    {
        "age": 3,
        "id": 4,
        "name": "Lassie"
    },
    {
        "age": 5,
        "id": 5,
        "name": "doggo"
    },
    {
        "age": 7,
        "id": 6,
        "name": "lorem"
    }
]


def connect():
    conn = sqlite3.connect('doggos.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS doggos (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.commit()
    conn.close()
    for i in doggos:
        bk = Doggo(getNewId(), i['name'], i['age'])
        insert(bk)


def insert(doggo):
    conn = sqlite3.connect('doggos.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO doggos VALUES (?,?,?)", (
        doggo.id,
        doggo.name,
        doggo.age
    ))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('doggos.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM doggos")
    rows = cur.fetchall()
    doggos = []
    for i in rows:
        doggo = Doggo(i[0], i[1], i[2])
        doggos.append(doggo)
    conn.close()
    return doggos


def update(doggo):
    conn = sqlite3.connect('doggos.db')
    cur = conn.cursor()
    cur.execute("UPDATE doggos SET name=?, age=? WHERE id=?",
                (doggo.name, doggo.age, doggo.id))
    conn.commit()
    conn.close()


def delete(theId):
    conn = sqlite3.connect('doggos.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM doggos WHERE id=?", (theId,))
    conn.commit()
    conn.close()


def deleteAll():
    conn = sqlite3.connect('doggos.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM doggos")
    conn.commit()
    conn.close()
