from bubblebooking.models import db


class Room(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    type = db.Column(db.String())
    features = db.Column(db.PickleType(list()))
    description = db.Column(db.String())

    def __init__(self, name, type, features, description):
        self.name = name
        self.type = type
        self.features = features
        self.description = description

    def get_room_info(self):
        return self.type, self.features
