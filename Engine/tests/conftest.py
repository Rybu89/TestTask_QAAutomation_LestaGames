import pytest
import pygame

from Engine.base.windows import Windows


@pytest.fixture(scope="module")
def set_up():
    print('Creation of window')
    pygame.init()

    yield
    print('Quit window')
    pygame.quit()
