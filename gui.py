from grid import Grid
from colors import BLACK, Color, WHITE
from point import Point
from itertools import product

import turtle as t

# By default, a square stamp is 20 x 20 pixels.
# This is also scale 1.0. So, to get a stamp that's 1 x 1 pixel
# need to pass in scale as 1/20
_TURTLE_DEFAULT_HEIGHT = 20
_TURTLE_DEFAULT_WIDTH = 20

_DEFAULT_MARGIN_LENGTH = 2
_DEFAULT_WINDOW_HEIGHT = 600


class GUI:

    def __init__(self,
                 grid: Grid,
                 window_height: int = _DEFAULT_WINDOW_HEIGHT,
                 window_width: int = None,
                 margin_len: int = _DEFAULT_MARGIN_LENGTH,
                 cell_color: Color = BLACK,
                 bg_color: Color = WHITE) -> None:
        """GUI to display pixels

        Args:
            grid (Grid): Grid object that contains data
            window_height (int): height of display window, in number of pixels
            window_width (int, optional): width of display window, in number of pixels. Defaults to None.
            margin_len (int, optional): margin between cells (pixels, hor, ver). Defaults to 2 pixels.
            cell_color (Color, optional): color of each cell. Defaults to BLACK (#000000).
            bg_color (Color, optional): color of background. Defaults to WHITE (#FFFFFF).
        """
        if window_width is None:
            window_width = window_height

        self.__grid = grid
        self.__window_height = window_height
        self.__window_width = window_width
        self.__margin_len = margin_len
        self.__cell_color = cell_color
        self.__bg_color = bg_color

        self.__grid.fill(self.__cell_color)
        # -------------------------- Setup turtle Parameters ------------------------- #
        t.screensize(
            canvwidth=window_width,
            canvheight=window_height
        )
        t.colormode(255)  # must have to support rbg color codes
        t.bgcolor(self.__bg_color)
        t.speed(0)  # max speed
        t.shape('square')  # change shape to square for stamping
        t.penup()
        t.setheading(0.0)
        t.hideturtle()

    def __calc_cell_width_height(self) -> tuple[int, int]:
        m = self.__margin_len
        width = (self.__window_width - (self.__grid.width() * m) +
                 m) // self.__grid.width()
        height = (self.__window_height - (self.__grid.height()
                                          * m) + m) // self.__grid.height()
        return width, height

    def __config_turtle_stamp(self, width: int, height: int) -> bool:
        if width <= 0 or height <= 0:
            return False
        t.turtlesize(width/_TURTLE_DEFAULT_WIDTH,
                     height/_TURTLE_DEFAULT_HEIGHT, 0)
        return True

    def render(self) -> bool:
        """ Render self.__grid colors

        Returns:
            bool: True if render successful, False otherwise
        """
        cell_w, cell_h = self.__calc_cell_width_height()
        if not self.__config_turtle_stamp(cell_w, cell_h):
            # Too many cells for the window
            return False
        start_x = (cell_w - self.__window_width)//2
        start_y = (self.__window_height - cell_h)//2
        # print(start_x, start_y)
        m = self.__margin_len
        # user tracer() and update() to speed up animation
        t.tracer(0, 0)
        for (x, y), c in self.__grid:
            new_x = start_x + x * (m + cell_w)
            new_y = start_y - y * (m + cell_h)
            # print(f'new_x: {new_x}, new_y: {new_y}, x: {x}, y: {y}')
            t.goto(new_x, new_y)
            t.color(c)
            t.stamp()
        t.update()

    def clear(self) -> None:
        self.__grid.refill()
        t.clearscreen()
        # After the above call, basically need to reinitialize turtle...
        t.colormode(255)  # must have to support rbg color codes
        t.bgcolor(self.__bg_color)
        t.speed(0)  # max speed
        t.shape('square')  # change shape to square for stamping
        t.penup()
        t.setheading(0.0)
        t.hideturtle()

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
        t.setup(window_width, window_height)  # width, height
        # set up grid
        self.__setup_grid(self.__grid.height(), self.__grid.width())
        t.screensize(
            canvwidth=window_width,
            canvheight=window_height
        )

    def draw_pixel(self, row: int, col: int) -> None:
        x, y = col * self.__pixel_size, row * self.__pixel_size
        t.penup()
        t.goto(x, y)
        t.color("black", "black")
        t.pendown()
        t.begin_fill()
        t.goto(x + self.__pixel_size, y)
        t.goto(x + self.__pixel_size, y + self.__pixel_size)
        t.goto(x, y + self.__pixel_size)
        t.goto(x, y)
        t.end_fill()
        t.penup()

    def draw_function(self, func) -> None:
        for x in range(self.__grid.width()):
            for y in range(self.__grid.height()):
                if func(x, y):
                    self.draw_pixel(x, y)

    # ------------------------------ Get Attributes ------------------------------ #

    def bg_color(self) -> Color:
        return self.__bg_color

    def window_height(self) -> int:
        return self.__window_height

    def window_width(self) -> int:
        return self.__window_width

    # ------------------------------ Set Attributes ------------------------------ #

    def set_bg_color(self, bg_color: Color) -> None:
        self.__bg_color = bg_color
        t.bgcolor(bg_color)

    def set_grid(self, grid: Grid) -> None:
        self.__grid = grid

    def set_window(self, height: int, width: int = None) -> None:
        if width is None:
            width = height
        self.__window_height = height
        self.__window_width = width


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
