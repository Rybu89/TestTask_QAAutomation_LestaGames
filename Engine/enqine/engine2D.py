from Engine.base.windows import *
from Engine.base.shapes import *
from Engine.base.inscriptions import *

class Engine2D:

    @staticmethod
    def create_a_canvas():
        """ Метод создания "холста". """

        canvas = Windows()
        return canvas.create_new_window(800, 350, 'White', "DrAw ShApEs")

    @staticmethod
    def create_static_figures(surface):
        """ Метод отрисовки статических фигур.
                Принимает:
                    surface - слой для отрисовки фигур (Str)
        """

        rectangle = Rectangle(layer=surface, color='Black', coordinates=[40, 20, 50, 50])
        rectangle.draw()

        circle = Circle(layer=surface, color='Blue', coordinates=(140, 45), radius=25)
        circle.draw()

        triangle = Triangle(layer=surface, color='Green', corner1=(190, 70), corner2=(250, 70), corner3=(220, 20))
        triangle.draw()

    @staticmethod
    def create_text_static_figures(surface):
        """ Метод создания подписи для статических фигур.
                Принимает:
                    surface - слой для отрисовки текста (Str)
        """

        text_static_figures = Inscriptions(
            surface=surface,
            font=(os.getcwd()+'\\..') +'\\recources\\Roboto_Black.ttf',
            font_size=25,
            text='To draw a shape, press " 1 ".',
            color='Red',
            coordinate_x=300,
            coordinate_y=20
        )
        text_static_figures.post_text()

    @staticmethod
    def create_text_dynamic_figures(surface):
        """ Метод создания подписи для динамических фигур.
                Принимает:
                    surface - слой для отрисовки текста (Str)
        """

        text_dynamic_figures = Inscriptions(
            surface=surface,
            font=(os.getcwd()+'\\..') +'\\recources\\Roboto_Black.ttf',
            font_size=18,
            text='Select the color of the shapes, press: 2-"Orange"; 3-"Blue"; 4-"Green".',
            color='Red',
            coordinate_x=50,
            coordinate_y=100
        )
        text_dynamic_figures.post_text()
    @staticmethod
    def choose_color_of_dynamic_figures(color, call_key):

        if call_key[pygame.K_2]:
            color = "Orange"
        elif call_key[pygame.K_3]:
            color = "Blue"
        elif call_key[pygame.K_4]:
            color = "Green"
        return color

    @staticmethod
    def create_dynamic_figures(color, surface):

        DynamicShapes(surface, color).draw_rect()
        DynamicShapes(surface, color).draw_circle()
        DynamicShapes(surface, color).draw_triangle()
        DynamicShapes(surface).clear()
