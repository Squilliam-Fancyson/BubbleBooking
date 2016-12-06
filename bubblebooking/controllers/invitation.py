"""Defines the controller for the Invitation model."""

from bubblebooking.models.scheduling.invitation import Invitation


class InvitationController(object):
    """Controls delivery and receipt of event invitations.

    Once a user creates an event, they can choose to send out invitations
    to other users. This controller handles the creation, modifications,
    and deletion of such invitations.

    """

    def _remove_pending_status(self, invite, accepted):
        """Modifies the status of an invite from pending.

        Args:
            invite (Invitation): The invite instance to modify.
            status (bool): The status to change the invite to.

        Raises:
            AttributeError: If *accepted* is not a truthy value.

        """
        assert accepted is not None

        if accepted:
            invite.accept()
        else:
            invite.decline()

    def accept_invite(self, invite):
        """Modifies an invitation to indicate a user has accepted it.

        Args:
            invite (Invitation): The invitation to accept.

        """
        self._remove_pending_status(invite, accepted=True)

    def decline_invite(self, invite):
        """Modifies an invitation to indicate a user has declined it.

        Args:
            invite (Invitation): The invitation to decline.

        """
        self._remove_pending_status(invite, accepted=False)

    def rsvp(self, user, event):
        """RSVP's a user to an event.

        Makes an invitation to an event for a given user and automatically
        accepts it. It then shows up as an accepted invitation to the
        event creator.

        Args:
            user (Account): User to add to attendee list.

            event (Event): Event to RSVP to.

        """
        inv = Invitation(user, event)
        db.session.add(inv)
        self.accept_invite(inv)
