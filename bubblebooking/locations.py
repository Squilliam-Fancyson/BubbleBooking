

class University(self, universityId, buildings):

    self.universityId = universityId
    self.buildings = buildings

class Building(self, buildingName, buildingId, rooms):

    self.buildingName = buildingName
    self.buildingId = buildingId
    self.rooms = rooms

class Room(self, roomName, roomNum, roomType, roomfeatures):

    #room attributes, room times not initialized???
    self.roomName = roomName
    self.roomNum = roomNum
    self.roomType = roomType
    self.roomFeatures = roomFeatures  #array
    self.roomTimes = []               #array, times not passed in?


