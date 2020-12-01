from grid import Grid
from colors import Color, WHITE
from point import Point

import turtle

class GUI:

    def __init__(self, grid: Grid, window_height: int = 600, window_width: int = None, bg_color: Color = WHITE) -> None:
        """GUI to display pixels

        Args:
            grid (Grid): Grid object that contains data
            window_height (int): height of display window, in number of pixels
            window_width (int, optional): width of display window, in number of pixels. Defaults to None.
            bg_color (Color, optional): color of background. Defaults to WHITE (#FFFFFF).
        """
        self.__grid = grid

        # setup turtle parameters
        turtle.colormode(255)  # must have to support rbg color codes
        turtle.speed(0)

        # set background color
        self.set_bg_color(bg_color)
        # setup window and calculate pixel size
        self.set_window(window_height, window_width)

        self.__t = turtle.Turtle()
        turtle.penup()        

    def __setup_grid(self, grid_height, grid_width) -> None:
        if grid_height > grid_width:
            self.__pixel_size = self.__window_height // grid_height
        else:
            self.__pixel_size = self.__window_width // grid_height

    def change_grid(self, height: int, width: int = None) -> None:
        self.__grid = Grid(height, width)
        self.__setup_grid(height, width)

    def set_window(self, window_height: int, window_width: int = None) -> None:
        if not window_width:
            window_width = window_height
        self.__window_height = window_height
        self.__window_width = window_width 
        turtle.setup(window_width, window_height) # width, height
        # set up grid
        self.__setup_grid(self.__grid.height(), self.__grid.width())
        turtle.screensize(
            canvwidth=window_width,
            canvheight=window_height
        )
        turtle.setworldcoordinates(0, 0, window_width, window_height)

    def set_bg_color(self, bg_color: Color) -> None:
        self.__bg_color = bg_color
        turtle.bgcolor(self.__bg_color)

    def bg_color(self) -> Color:
        return self.__bg_color

    def window_height(self) -> int:
        return self.__window_height

    def window_width(self) -> int:
        return self.__window_width

    def draw_pixel(self, row: int, col: int) -> None:
        x, y = col * self.__pixel_size, row * self.__pixel_size 
        turtle.penup()
        self.__t.goto(x, y)
        turtle.color("black", "black")
        turtle.pendown()
        self.__t.begin_fill()
        self.__t.goto(x + self.__pixel_size, y)
        self.__t.goto(x + self.__pixel_size, y + self.__pixel_size)
        self.__t.goto(x, y + self.__pixel_size)
        self.__t.goto(x, y)
        self.__t.end_fill()
        turtle.penup()

    def draw_function(self, func) -> None:
        for x in range(self.__grid.width()):
            for y in range(self.__grid.height()):
                if func(x, y):
                    self.draw_pixel(x, y)

    # def render(self) -> None:
    #     t.colormode(255)  # must have to support rbg color codes
    #     t.bgcolor(self.__bg_color)
    #     t.screensize(
    #         canvwidth=self.__grid.width(),
    #         canvheight=self.__grid.height()
    #     )

    def clear(self) -> None:
        turtle.clearscreen()

"""
Example script:
import grid, gui
test_grid = grid.Grid(3,3)
window = gui.GUI(test_grid)

func = lambda x, y: x == y
window.draw_function(func)
window.clear()

func = lambda x, y: (x + y) % 2 == 0
window.draw_function(func)
window.change_grid(9, 9)
window.draw_function(func)
"""
