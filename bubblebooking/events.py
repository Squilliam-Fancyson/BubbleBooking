

class Events(object):

    def __init__(self, eventId, eventName, buildingId, roomNum):
        self.eventId = eventId
        self.eventName = eventName
        self.eventBuilding = buildingId
        self.roomNum = roomNum
        self.date
        self.time
        self.organizer
        self.attendees #array
        self.maxOccupancy

    #create and cancel events
    def createEvent(self, eventId):
        #CHECK AVAILABILITY AND THEN BOOK ROOM

    def viewEvent(selfs):
        #CHECK IF EVENT EXISTS THEN DISPLAY

    def cancelEvent(self, event_id):
        #CHECK PERMISSIONS, CHECK IF EVENT EXISTS, DELETE EVENT

    def RSVP(self, event_id, acct_id):
        #CHECK IF EVENT EXISTS, CHECK OCCUPANCY, RSVP


