from bubblebooking.models import db


class University(db.Model):
    buildings = db.Column(db.PickleType(list()))

    def __init__(self):
        pass
