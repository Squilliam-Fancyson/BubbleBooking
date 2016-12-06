"""Controls room booking for scheduling events.

This controller serves the Room, Event, and Account models.

Attributes:
    state (str): Indicates the availability between a Room and Event instance.

    invitee (Account): Indicates the booker of a room between an Account and Event.

    best_fit_criteria: The criteria required to search for a best fit for a room.

Methods:
    get_best_fit (Room): Find the room that best fits the requirements for an event.

    book_event: Books a specified event with a room.

    cancel_booking: Unbooks a specified event from a room.

    create_event (Event): Creates an Event instance.

"""
