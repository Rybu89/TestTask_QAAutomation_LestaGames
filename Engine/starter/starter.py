import pygame
from Engine.enqine.engine2D import *

engine = Engine2D()

pygame.init()

# Window
window = engine.create_a_canvas()
engine.create_static_figures(window)
engine.create_text_static_figures(window)
engine.create_text_dynamic_figures(window)

# Dynamic
run = True
color_dynamic_figure = "Red"
while run:

    # Actions
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    call_keys = pygame.key.get_pressed()
    if call_keys[pygame.K_2] or [pygame.K_3] or [pygame.K_4]:
        color_dynamic_figure = engine.choose_color_of_dynamic_figures(color_dynamic_figure, call_keys)
        if call_keys[pygame.K_1]:
            engine.create_dynamic_figures(color_dynamic_figure, window)

    pygame.display.update()

pygame.quit()
