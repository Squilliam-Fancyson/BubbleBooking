"""Defines the controller for the Room model."""


from bubblebooking.models import db
from bubblebooking.models.locations.room import Room
from bubblebooking.models.scheduling.event import Event
from bubblebooking.forms import BestFitCriteriaForm


class RoomController(object):
    """Controls room booking for scheduling events.

    Attributes:
        best_fit_criteria (WTForms.Form): The criteria required to search for
        the best-fitting room for an event.

    Methods:
        get_best_fit: Find the room that best fits the requirements for an event.

        book_event: Books a specified event with a room.

        cancel_booking: Unbooks a specified event from a room.

        create_event: Creates an Event instance.

    """

    bestfit_criteria = BestFitCriteriaForm()

    def __init__(self):
        self.bestfit_criteria = bestfit_criteria

    def get_best_fit(self):
        """Get available rooms for given event parameters."""
        rooms = []
        # TODO: Implement best fit algorithm.
        rooms.append(Room("Test Room", "Test", ["Test1", "Test2"], "Test Descr."))
        return rooms

    def book_event(self, user, event):
        """Book a specified event with a room.

        Args:
            user (Account):

            event (Event): Event to book a room for.

        """
        # if USER has BOOKING_PERMISSION
        #### create EVENT
        #### set EVENT.ORGANIZER to USER
        db.session.add(event)

    def cancel_booking(self, event):
        """Unbook an event from its room.

        Args:
           event (Event): Event to unbook a room from.

        """
        # if USER is EVENT.ORGANIZER or USER.hasPermission(cancelOther)
        db.session.expunge(event)

    def create_event(self, name, room, organizer):
        """Create an event.

        Args:
            name (str): Name of the event.

            room (Room): Room of the event.

            organizer (Account): Organizer of the event.

        """
        # if (ROOM.day.timeslot[slot] == "available")
        #### and (USER.hasPermission(createEvent))
        event = Event(name, room, organizer)
        db.session.add(event)
        return event
