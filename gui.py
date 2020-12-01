from grid import Grid
from colors import Color, WHITE
from point import Point

import turtle as t


class GUI:

    def __init__(self, grid: Grid, window_height: int, window_width: int = None, bg_color: Color = WHITE) -> None:
        """GUI to display pixels

        Args:
            grid (Grid): Grid object that contains data
            window_height (int): height of display window, in number of pixels
            window_width (int, optional): width of display window, in number of pixels. Defaults to None.
            bg_color (Color, optional): color of background. Defaults to WHITE (#FFFFFF).
        """
        if not window_width:
            window_width = window_height
        self.__grid = grid
        self.__window_height = window_height
        self.__window_width = window_width
        self.__bg_color = bg_color

    def set_bg_color(self, bg_color: Color) -> None:
        self.__bg_color = bg_color

    def bg_color(self) -> Color:
        return self.__bg_color

    def window_height(self) -> int:
        return self.__window_height

    def window_width(self) -> int:
        return self.__window_width

    def render(self) -> None:
        t.colormode(255)  # must have to support rbg color codes
        t.bgcolor(self.__bg_color)
        t.screensize(
            canvwidth=self.__grid.width(),
            canvheight=self.__grid.height()
        )
