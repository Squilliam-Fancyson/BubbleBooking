from flask_sqlalchemy import SQLAlchemy

from bubblebooking.models import db
from bubblebooking.models.locations.room import Room

class Building(db.Model):
    self.bldg_id = db.Column("building ID", db.Integer(), primary_key=True)
    self.name = db.Column(db.String())
    self.address = db.Column(db.String())
    self.rooms = db.Column(db.PickleType(list())

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def add_room(self, room):
        self.rooms.append(room)

    def __repr__(self):
        return "<Building {name}>".format(name=self.bldg_name)
