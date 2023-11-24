import os
import time
from Engine.base.inscriptions import *


class Shapes:
    """ Класс создания геометрических фигур. """

    def __init__(self, layer, color):
        self.layer = layer
        self.color = color

class Rectangle(Shapes):
    """ Создание прямоугольника. """

    def __init__(self, layer, color, coordinates):
        super().__init__(layer, color)
        self.coordinates = coordinates

    def draw(self):
        pygame.draw.rect(surface=self.layer, color=self.color, rect=self.coordinates)

class Circle(Rectangle):
    """ Создание окружности. """

    def __init__(self, layer, color, coordinates, radius):
        super().__init__(layer, color, coordinates)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(surface=self.layer, color=self.color, center=self.coordinates, radius=self.radius)

class Triangle(Shapes):
    """ Создание треугольника. """

    def __init__(self, layer, color, corner1, corner2, corner3):
        super().__init__(layer, color)
        self.corner1 = corner1
        self.corner2 = corner2
        self.corner3 = corner3

    def draw(self):
        pygame.draw.polygon(surface=self.layer, color=self.color, points=[self.corner1, self.corner2, self.corner3])

class DynamicShapes:
    def __init__(self, layer, color=None):
        self.layer = layer
        self.color = color

    def draw_rect(self):
        new_surface = pygame.Surface((600, 300))
        new_surface.fill('White')
        pygame.draw.rect(new_surface, color=self.color, rect=[40, 20, 50, 50])
        Inscriptions(
            surface=new_surface,
            font=os.getcwd() +'\\Roboto-Black.ttf',
            font_size=35,
            text=f"Drawing Rectangle:{self.color}",
            color=self.color,
            coordinate_x=60,
            coordinate_y=70
        ).post_text()
        self.layer.blit(new_surface, (100, 200))
        pygame.display.update()
        time.sleep(0.5)

    def draw_triangle(self):
        new_surface = pygame.Surface((600, 300))
        new_surface.fill('White')
        pygame.draw.polygon(surface=new_surface, color=self.color, points=[(190, 70), (250, 70), (220, 20)])
        Inscriptions(
            surface=new_surface,
            font=os.getcwd() +'\\Roboto-Black.ttf',
            font_size=35,
            text=f"Drawing Triangle:{self.color}",
            color=self.color,
            coordinate_x=60,
            coordinate_y=70
        ).post_text()
        self.layer.blit(new_surface, (100, 200))
        pygame.display.update()
        time.sleep(0.5)

    def draw_circle(self):
        new_surface = pygame.Surface((600, 300))
        new_surface.fill('White')
        pygame.draw.circle(new_surface, color=self.color, center=(140, 45), radius=25)
        Inscriptions(
            surface=new_surface,
            font=os.getcwd() +'\\Roboto-Black.ttf',
            font_size=35,
            text=f"Drawing Circle:{self.color}",
            color=self.color,
            coordinate_x=60,
            coordinate_y=70
        ).post_text()
        self.layer.blit(new_surface, (100, 200))
        pygame.display.update()
        time.sleep(0.5)

    def clear(self):
        new_surface = pygame.Surface((600, 300))
        new_surface.fill('White')
        self.layer.blit(new_surface, (100, 200))
        pygame.display.update()
