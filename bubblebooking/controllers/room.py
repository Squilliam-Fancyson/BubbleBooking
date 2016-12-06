"""Defines the controller for the Room model."""

from flask_wtforms import WTForms

from bubblebooking.models.locations.room import Room
from bubblebooking.models.accounts import Account
from bubblebooking.models.scheduling import Event


class RoomController(object):
    """Controls room booking for scheduling events.
    
    Attributes:
        state (str): Indicates the availability between a Room and Event instance.
        
        user (Account): Indicates the booker of a room between an Account and Event.
        
        best_fit_criteria (collections.namedtuple): The criteria required to search for 
        the best-fitting room for an event.
    
    Methods:
        get_best_fit: Find the room that best fits the requirements for an event.
        
        book_event: Books a specified event with a room.
        
        cancel_booking: Unbooks a specified event from a room.
        
        create_event: Creates an Event instance.
    
    """
    
    self.state = str()
    self.user = Account()
    self.bestfit_criteria = WTForms()
    
    def __init__(self, state=None, invitee=None, bestfit_criteria=None):
        self.state = state
        self.user = invitee
        self.bestfit_criteria = bestfit_criteria

    def get_best_fit(self) -> list:
        """Get available rooms for given event parameters."""
        rooms = []
        # TODO: Implement best fit algorithm.
        return rooms
    
    def book_event(self, event: Event)
        """Book a specified event with a room.
        
        Args:
            event (Event): Event to book a room for.
        
        """
        # TODO: Add event to database.
        
    
    def cancel_booking(self, event: Event):
        """Unbook an event from its room.
        
        Args:
           event (Event): Event to unbook a room from."""
        
        """
        # TODO: Remove event from database.
