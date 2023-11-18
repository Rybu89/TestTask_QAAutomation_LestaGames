import time

import pygame
from shapes import Square

from canvas import Canvas

canvas = Canvas()


class Engine2D:

    pygame.init()
    screen = canvas.create_new_window(600, 800, 'White', "DrAw ShApEs")
    square = Square(layer=screen, color='Red', rect=[20, 20, 50, 50])
    pygame.display.update()
    time.sleep(5)
    square.print()
    pygame.display.update()
    time.sleep(5)
    canvas.create_new_window(600, 800, 'White', "DrAw ShApEs")
    run = True
    while run:
        # pygame.draw.rect(surface=screen, color='Red', rect=[20, 20, 50, 50])
        # pygame.draw.circle(surface=screen, color='Red', center=(20, 100), radius=50)
        # pygame.draw.polygon(surface=screen, color='Red', points=[(400, 100), (200, 400), (600, 400)])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()




    # def create_shape(self,
    #                  параметра):