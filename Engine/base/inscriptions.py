import pygame

class Inscriptions:

    def __init__(self, surface, font, font_size, text, color, coordinate_x, coordinate_y):

        self.surface = surface
        self.font = font
        self.font_size = font_size
        self.color = color
        self.text = text
        self.font_size = font_size
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def post_text(self):
        """ Метод размещения текста на слоях. """

        font1 = pygame.font.Font(self.font, self.font_size).render(self.text, True, self.color)
        self.surface.blit(font1, (self.coordinate_x, self.coordinate_y))
        return font1
