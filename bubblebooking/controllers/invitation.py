"""Defines the controller for the Invitation model."""

from bubblebooking.models.accounts import Account
from bubblebooking.models.scheduling import Invitation
from bubblebooking.controllers.room import RoomController


class InvitationController(object):
    """Controls delivery and receipt of event invitations.
    
    Once a user creates an event, they can choose to send out invitations
    to other users. This controller handles the creation, modifications,
    and deletion of such invitations.
    
    """

    def _remove_pending_status(invite: Invitation, accepted: bool):
        """Modifies the status of an invite from pending.
        
        Args:
            invite (Invitation): The invite instance to modify.
            status (bool): The status to change the invite to.
        
        Raises:
            AttributeError: If *accepted* is not a truthy value.
            
        """
        if accepted is None:
            raise AttributeError("Invite must be accepted or declined.")
        if accepted:
            invite.accept()
        else:
            invite.decline()

    def rsvp(user: Account, room_ctr: RoomController):
        """RSVP's a user to an event.
        
        Args:
            user (Account): User to add to attendee list.
            
            room_ctr (RoomController): RoomController for the designated event.
        
        """
        room_ctr.add_user_to_attendees(user)

    def accept_invite(invite: Invitation):
        """Modifies an invitation to indicate a user has accepted it.
        
        Args:
            invite: The invitation to accept.
        
        """
        _remove_pending_status(invite, accepted=True)

    def decline_invite(invite: Invitation):
        """Modifies an invitation to indicate a user has declined it.
        
        Args:
            invite: The invitation to decline.
        
        """
        _remove_pending_status(invite, accepted=False)
