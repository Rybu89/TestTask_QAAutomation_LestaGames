from Engine.base.shapes import DynamicShapes
from Engine.base.windows import *

class TestShapesCreation:
    window = Windows().create_new_window(300, 300, "White", "Tot")

    def test_create_new_window(self, set_up):
        assert isinstance(self.window, pygame.surface.Surface), \
            f"The layer type does not match the expected one"
        assert self.window.get_size() == (300, 300), \
            f"The layer size does not match the expected one. Actual size: {self.window.get_size()}"
        assert self.window.get_at((299, 299)) == (255, 255, 255, 255), \
            f"The color of the layer does not match the expected one. The actual color of the layer: " \
            f"RGBA{self.window.get_at((299, 299))}"
        assert pygame.display.get_caption()[0] == "Tot", \
            f"The name of the layer does not match what is expected. Actual name:{pygame.display.get_caption()[0]}"

    def test_draw_rect(self):
        dynamic_shapes = DynamicShapes(self.window, "Yellow")
        surface = dynamic_shapes.draw_rect()
        assert surface.get_at((599, 299)) == (255, 255, 255, 255), \
            f"The color of the layer does not match the expected one. The actual color of the layer: " \
            f"RGBA{surface.get_at((599, 229))}"
        assert surface.get_at((41, 21)) == (255, 255, 0, 255), \
            f"The color of the rectangle does not match the expected one. The actual color of the " \
            f"rectangle: RGBA{surface.get_at((41, 21))}"

    def test_draw_triangle(self):
        dynamic_shapes = DynamicShapes(self.window, "Yellow")
        surface = dynamic_shapes.draw_triangle()
        assert surface.get_at((190, 69)) == (255, 255, 255, 255), \
            f"The color of the layer does not match the expected one. The actual color of the layer: " \
            f"RGBA{surface.get_at((190, 69))}"
        assert surface.get_at((190, 70)) == (255, 255, 0, 255), \
        f"The color of the triangle does not match the expected one. The actual color of the triangle: " \
        f"RGBA{surface.get_at((190, 70))}"

    def test_draw_circle(self):
        dynamic_shapes = DynamicShapes(self.window, "Yellow")
        surface = dynamic_shapes.draw_circle()
        assert surface.get_at((140, 71)) == (255, 255, 255, 255), \
            f"The color of the layer does not match the expected one. The actual color of the layer: " \
            f"RGBA{surface.get_at((140, 45))}"
        assert surface.get_at((140, 45)) == (255, 255, 0, 255), \
            f"The color of the circle does not match the expected one. The actual color of the circle: " \
            f"RGBA{surface.get_at((140, 45))}"
