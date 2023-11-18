import pygame

class Canvas():

    def create_new_window(self, x, y, background_color, name):
        new_window = pygame.display.set_mode((x, y))
        new_window.fill(background_color)
        pygame.display.set_caption(name)
        return new_window



