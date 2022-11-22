from dogs import db
from dogs import app

with app.app_context():
    db.drop_all()

    db.create_all()
