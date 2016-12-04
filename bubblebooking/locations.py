

class University(self, name, universityId, buildings):

    self.name
    self.universityId = universityId
    self.buildings = buildings

class Building(self, buildingName, buildingId, address, rooms, buildingHours):

    self.buildingName = buildingName
    self.buildingId = buildingId
    self.address = address #struct
    self.rooms = rooms     #array
    self.buildingHours #array

class Room(self, roomName, roomNum, roomType, roomfeatures):

    #room attributes, room times not initialized???
    self.roomName = roomName
    self.roomNum = roomNum
    self.roomType = roomType
    self.roomFeatures = roomFeatures  #array
    self.roomTimes = []               #array, times not passed in?


    def book(self, date, time):
        #todo

    def unbook(self, date, time):
        #todo

