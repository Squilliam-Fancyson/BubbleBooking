from bubblebooking.models import db


class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    rooms = db.Column(db.PickleType(list()))

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return "<Building {name}>".format(name=self.bldg_name)
