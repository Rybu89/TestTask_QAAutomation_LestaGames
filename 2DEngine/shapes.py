import pygame
from canvas import Canvas


# @dataclasses
# class Shapers():
#     name: str
#     color: str = 'White'
#     height: int
#     width: int
#
#     # pygame.Surface((600, 100))

class Shapes:

    def __init__(self, color, layer):
        self.color = color
        self.layer = layer

    def print(self):
        pass


class Square(Shapes):

    def __init__(self, color, layer, rect):
        super().__init__(color, layer)
        self.rect = rect
        # pygame.draw.rect(surface=self.layer, color=self.color, rect=rect)

    def print(self):
        return pygame.draw.rect(surface=self.layer, color=self.color, rect=self.rect)
