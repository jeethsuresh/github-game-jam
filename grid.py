from item import Wall, Turret, Minion 

class GridSquare():
    x = 0
    y = 0
    size = 0
    contains = ""

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def PutInSquare(self, toput):
        self.contains = toput
    
    def CollidesWithPoint(self, x, y):
        if x > self.x and x < (self.x + self.size) and y > self.y and y < (self.y + self.size):
            return True
        return False

class Grid():
    grid = []
    grid_height = 45
    grid_width = 45
    def __init__(self, square_size):
        for x in range(0, self.grid_width):
            grid_row = []
            for y in range(0, self.grid_height):
                gridsquare = GridSquare(x*square_size, y*square_size, square_size)
                grid_row.append(gridsquare)
            self.grid.append(grid_row)
        
    def GetGrid(self):
        return self.grid

class InventorySquare():
    x = 0
    y = 0
    size = 0
    contains = ""
    
    def __init__(self, x, y, size, contains):
        self.x = x
        self.y = y
        self.size = size
        self.contains = contains
    
    def setContains(self, item):
        self.contains = item

    def CollidesWithPoint(self, x, y):
        if x > self.x and x < (self.x + self.size) and y > self.y and y < (self.y + self.size):
            return True
        return False
    
class Inventory():
    items = [Wall("wall"), Turret("turret"), Minion("minion")]
    inventory = []
    gridLength = 0
    sideLength = 0
    width = 0

    def __init__(self, gridLength, sideLength, width):
        self.gridLength = gridLength
        self.sideLength = sideLength
        self.width = width
        self.__populateInventory()
    
    def __populateInventory(self):
        for i in xrange(0, len(self.items)):
            x = self.gridLength * self.sideLength
            y = self.width * i
            self.inventory.append(InventorySquare(x, y, self.width, self.items[i].GetString()))
    
    def GetInventory(self):
        return self.inventory

