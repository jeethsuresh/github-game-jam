"""Main file"""
import pygame
from grid import Grid, Inventory

MAX_FRAMES = 60
VELOCITY = 3

def main():
    """main function"""
    print("test")
    pygame.init()

    size = [1000, 900]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("ASDF TEST")
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 10)
    
    done = False

    clock = pygame.time.Clock()

    grid = Grid(20).GetGrid()
    inventory = Inventory(45, 20, 100).GetInventory()

    is_blue = True
    selectedItem = inventory[0].contains
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousecursor = pygame.mouse.get_pos()
                for rect_row in grid:
                    for rect in rect_row:
                        if rect.CollidesWithPoint(mousecursor[0], mousecursor[1]):
                            rect.PutInSquare(selectedItem)
                for inventory_item in inventory:
                    if inventory_item.CollidesWithPoint(mousecursor[0], mousecursor[1]):
                        selectedItem = inventory_item.contains

        pressed = pygame.key.get_pressed()

        screen.fill((255, 255, 255))
        for rect_row in grid: 
            for rect in rect_row:
                thisrect = pygame.Rect(rect.x, rect.y, rect.size, rect.size)
                pygame.draw.rect(screen,(255, 100, 0), thisrect, 1)
                textsurface = myfont.render(rect.contains, False, (0, 0, 0))
                screen.blit(textsurface,(rect.x + 3, rect.y + 3))
        
        inventoryRect = pygame.Rect(45*20, 0, 100, 45*20)
        pygame.draw.rect(screen, (0,0,0), inventoryRect, 1)    
        for inv_square in inventory:
            itemRect = pygame.Rect(inv_square.x, inv_square.y, inv_square.size, inv_square.size)
            pygame.draw.rect(screen, (0, 0, 0), itemRect, 1)
            textsurface = myfont.render(inv_square.contains, False, (0, 0, 0))
            screen.blit(textsurface,(inv_square.x + 30, inv_square.y + 30))
          
        clock.tick(MAX_FRAMES)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    