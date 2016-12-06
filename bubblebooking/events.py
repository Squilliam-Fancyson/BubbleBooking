

class Events(object):

    def __init__(self, eventName, eventRoom, organizer, attendees, date):

        self.eventName = eventName
        self.eventRoom = eventRoom
        self.eventOrganizer = organizer
        self.eventAttendees = attendees
        self.eventDate = date

    def destroy(eventId):
        if self.organizer.hasPermissions(self.eventOrganizer.userName) == True:
            #deleteEvent

    def addUsertoAttendingList(userId):
        #TODO

class Day(timeSlots):
    self.dayTimeSlots = timeSlots

    def isAvailable(time):
        #todo

    def reserve(time):
        if self.organizer.hasPermissions(self.eventOrganizer.userName) == True:
            #reserveEvent

class Invitation(object, state, invitee):

        def __init__(self):
            self.inviteState = state
            self.invitee = invitee

        def acceptInvite(invitee):
            removePendingStatus()
            AddUserToAttendingList(invitee)


        def declineInvite():
            #todo

        def removePendingStatus():
            #todo


