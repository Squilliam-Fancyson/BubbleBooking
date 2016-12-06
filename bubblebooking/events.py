

class Events():
    def __init__(self, eventName, eventRoom, organizer, attendees, date):
        self.eventName = eventName
        self.eventRoom = eventRoom
        self.eventOrganizer = organizer
        self.eventAttendees = attendees
        self.eventDate = date

    def destroy(self, eventId):
        if self.organizer.hasPermissions(self.eventOrganizer.userName) == True:
        #deleteEvent

    def addUsertoAttendingList(self, userId):
        self.eventAttendees.append(userId)

class Day(Events):

    def __init__(self, timeSlots):
        self.dayTimeSlots = timeSlots

    def isAvailable(self, timeSlots):
        #todo

    def reserve(self, reserveTimeSlots):
        if self.organizer.hasPermissions(self.eventOrganizer.userName) == True:
            for i in reserveTimeSlots:
                for j in self.timeSlots:
                    if reserveTimeSlots[i] == self.timesSlots[j]:
                        return 0
                    else:
                        self.timeSlots[j] = reserveTimeSlots[i]


class Invitation(Events):

        def __init__(self, state, invitee):
            self.inviteState = state
            self.invitee = invitee

        def acceptInvite(self, invitee):
            self.Invitation.removePendingStatus()
            self.AddUserToAttendingList(invitee)

        def declineInvite(self, invitee):
            self.Invitation.removePendingStatus()

        def removePendingStatus(self, invitee):
            invitee.removePendingStatus()


