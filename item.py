class Item():
    stringRepresentation = ""
    description = ""
    name = ""
        
    def GetName(self):
        return self.name 

    def GetString(self):
        return self.stringRepresentation

class Wall(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = stringRepresentation[0]
        self.name = stringRepresentation

class Turret(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = stringRepresentation[0]
        self.name = stringRepresentation

class Minion(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = stringRepresentation[0]
        self.name = stringRepresentation

class Waypoint(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = stringRepresentation[0]
        self.name = stringRepresentation

class Clear(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = ""
        self.name = stringRepresentation