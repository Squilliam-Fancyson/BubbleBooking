from bubblebooking.models import db


class Day(db.Model):
    id = db.Column(db.Date(), primary_key=True)
    timeslots = db.Column(db.PickleType({str(x): True for x in range(1, 25)}))

    def is_available(self, time):
        return self.timeslots[time]

    def reserve(self, time):
        self.timeslots[time] = False
