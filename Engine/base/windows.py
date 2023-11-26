import pygame

class Windows:
    def __init__(self):
        pass

    @staticmethod
    def create_new_window(x, y, background_color=None, name=None):
        """ Метод создания окна с холстом"""

        new_window = pygame.display.set_mode((x, y))
        new_window.fill(background_color)
        pygame.display.set_caption(name)

        return new_window
