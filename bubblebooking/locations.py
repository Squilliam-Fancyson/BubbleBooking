

class University(object):

    def __init(self, univName, univId, buildings):
        self.name = univName
        self.universityId = univId
        self.buildings = buildings

class Building(object):

    def __init__(self, buildingName, buildingId, address, rooms, buildingHours):
        self.buildingName = buildingName
        self.buildingId = buildingId
        self.address = address #struct
        self.rooms = rooms     #array
        self.buildingHours = buildingHours #array

class Room(object):
    def __init__(self, roomName, roomNum, roomType, roomFeatures, roomMaxOccupancy):

        self.roomName = roomName
        self.roomNum = roomNum
        self.roomType = roomType
        self.roomMaxOccupancy = roomMaxOccupancy
        self.roomFeatures = roomFeatures  #array
        self.roomTimes = []

    def book(self, date, time):
        #CHECK ROOM TIME

    def unbook(self, date, time):
        #CHECK IF EVENT EXISTS, CHECK PERMISSIONS, UNBOOK

