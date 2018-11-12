class Item():
    stringRepresentation = ""
    description = ""
        
    def GetString(self):
        return self.stringRepresentation

class Wall(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = stringRepresentation

class Turret(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = stringRepresentation

class Minion(Item):

    def __init__(self, stringRepresentation):
        self.stringRepresentation = stringRepresentation