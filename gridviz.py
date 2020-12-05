from typing import Callable

from grid import Grid
from gui import GUI
from colors import BLACK, Color, WHITE
from inspect import signature

"""Main file

This also acts as the controller of the visualizer
"""
_DEFAULT_CELL_COLOR = BLACK
_DEFAULT_BG_COLOR = WHITE

_DEFAULT_MARGIN_LENGTH = 2
_DEFAULT_WINDOW_HEIGHT = 600


class Viz:
    
    def __init__(self, 
                 height: int,
                 width: int = None,
                 window_height: int = _DEFAULT_WINDOW_HEIGHT,
                 window_width: int = None,
                 margin_len: int = _DEFAULT_MARGIN_LENGTH,
                 cell_color: Color = _DEFAULT_CELL_COLOR,
                 bg_color: Color = _DEFAULT_BG_COLOR) -> None:
              
        self.grid = Grid(height, width, cell_color)
        
        self.gui = GUI(self.grid,
                       window_height,
                       window_width, 
                       margin_len, 
                       cell_color, 
                       bg_color)
        
        self.gui.render()


    def reset(self) -> None:
        """Reset to original settings and redraw canvas
        """
        self.gui.reset()
        self.gui.render()

    def __process_func(self, func: Callable) -> Callable:
        sig = signature(func)
        params = sig.parameters
        p_len = len(params)
        if p_len == 1:
            return lambda x, y, o: func(o)
        elif p_len == 2:
            return lambda x, y, o: func(x, y)
        elif p_len == 3:
            return func
        else:
            return None

    def filter(self, func: Callable) -> None:
        f = self.__process_func(func)
        if not f:
            print("Invalid input function")
            return
        self.grid.transform(self.gui.bg_color(), f)
        self.gui.clear_screen()
        self.gui.render()
        
        
    def map(self, func: Callable) -> None:
        f = self.__process_func(func)
        if not f:
            print("Invalid input function")
            return
        self.grid.apply(f)
        self.gui.clear_screen()
        self.gui.render()


    # ----------------------------------- Debug ---------------------------------- #
    
    def _print_grid(self) -> None:
        print(self.grid)
