from bubblebooking.models import db
from bubblebooking.models.accounts import Account


class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Enum("pending", "accepted", "declined",
                              name="StateEnum"))
    invitee = db.relation(Account)

    def _remove_pending_status(self, accepted):
        if accepted:
            self.state = "accepted"
        else:
            self.state = "declined"

    def accept_invite(self):
        self._remove_pending_status(True)

    def decline_invite(self):
        self._remove_pending_status(False)
