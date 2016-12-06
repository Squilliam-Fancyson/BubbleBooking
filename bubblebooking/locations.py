

class University(object):

    def __init__(self, univId, buildings):
        self.universityId = univId
        self.buildings = buildings

class Building(object):

    def __init__(self, buildingName, buildingId, address, rooms):
        self.buildingName = buildingName
        self.buildingId = buildingId
        self.address = address #struct
        self.rooms = rooms     #array

class Room(object):
    def __init__(self, roomId, roomName, roomType, roomFeatures, roomDescription):

        self.roomName = roomName
        self.roomId = roomId
        self.roomType = roomType
        self.roomFeatures = roomFeatures  #array
        self.description = roomDescription

    def getRoomInfo(self, roomId):
        #todo


