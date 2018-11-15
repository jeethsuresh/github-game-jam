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

    start_square = (0,0)
    end_square = (0,0)
    current_square = (-1,-1)
    mouse_button_pressed = False
    is_blue = True
    selectedItem = inventory[0].contains.GetString()
    selectrect = pygame.Rect(0,0,0,0)
    while not done:
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0,255,255,64), selectrect)
        for event in pygame.event.get():
            mousecursor = pygame.mouse.get_pos()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                done = True
            if mouse_button_pressed:                                
                selectrect = pygame.Rect(min(start_square[0] * 20, mousecursor[0]), min(start_square[1] * 20,mousecursor[1]) , abs(start_square[0] * 20 - mousecursor[0]) , abs(start_square[1] * 20 - mousecursor[1]))
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                current_square = (-1,-1)
                for rect_row in grid:
                    current_square = (current_square[0] + 1, -1)
                    for rect in rect_row:
                        current_square = (current_square[0], current_square[1] + 1)
                        if rect.CollidesWithPoint(mousecursor[0], mousecursor[1]):
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                start_square = current_square
                                mouse_button_pressed = True
                            elif mouse_button_pressed:
                                end_square = current_square
                            if event.type == pygame.MOUSEBUTTONUP:
                                if start_square == end_square:
                                    grid[start_square[0]][start_square[1]].PutInSquare(selectedItem)
                                else:
                                    for x in range(min(start_square[0], end_square[0]), max(start_square[0],end_square[0] ) + 1):
                                        for y in range(min(start_square[1], end_square[1]), max(start_square[1],end_square[1]) + 1):
                                            grid[x][y].PutInSquare(selectedItem)
                                start_square = (0,0)
                                end_square = (0,0)
                                mouse_button_pressed = False    
                                selectrect = pygame.Rect(0,0,0,0)
                for inventory_item in inventory:
                    if inventory_item.CollidesWithPoint(mousecursor[0], mousecursor[1]):
                        selectedItem = inventory_item.contains.GetString()

        pressed = pygame.key.get_pressed()
        
        # if mouse_button_pressed:                                
        #     selectrect = pygame.Rect(min(start_square[0] * 20, current_square[0] * 20), min(start_square[1] * 20,current_square[1] * 20), abs(start_square[0]* 20 - current_square[0] * 20) + 20, abs(start_square[1]*20 - current_square[1]*20) + 20 )
        #     pygame.draw.rect(screen, (255,0,0),selectrect)

        for rect_row in grid: 
            for rect in rect_row:
                thisrect = pygame.Rect(rect.x, rect.y, rect.size, rect.size)
                pygame.draw.rect(screen,(255, 100, 0), thisrect, 1)
                textsurface = myfont.render(rect.contains, False, (0, 0, 0))
                screen.blit(textsurface,(rect.x +3, rect.y + 3))
        
        inventoryRect = pygame.Rect(45*20, 0, 100, 45*20)
        pygame.draw.rect(screen, (0,0,0), inventoryRect, 1)    
        for inv_square in inventory:
            itemRect = pygame.Rect(inv_square.x, inv_square.y, inv_square.size, inv_square.size)
            pygame.draw.rect(screen, (0, 0, 0), itemRect, 1)
            textsurface = myfont.render(inv_square.contains.GetName(), False, (0, 0, 0))
            screen.blit(textsurface,(inv_square.x + 10, inv_square.y + 10))
          
        clock.tick(MAX_FRAMES)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    