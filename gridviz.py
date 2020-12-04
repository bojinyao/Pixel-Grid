from grid import Grid
from gui import GUI
from inspect import signature

"""Main file

This also acts as the controller of the app
"""

_DEFAULT_W_HEIGHT = 600


class Viz:
    
    def __init__(self, 
                 height: int,
                 width: int = None,
                 window_height: int = _DEFAULT_W_HEIGHT,
                 window_width: int = None) -> None:        
        self.__grid = Grid(height, width)
        self.__gui = GUI(self.__grid, window_height, window_width)
        

    def display(self) -> None:
        """Update Display
        """
        self.__gui.render()


    def reset(self) -> None:
        """Reset to original settings and redraw canvas
        """
        self.__grid.refill()
        self.__gui.clear()
        self.__gui.render()

    def __process_func(self, func: function) -> function:
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

    def filter(self, func: function) -> None:
        f = self.__process_func(func)
        if not f:
            print("Invalid input function")
            return
        self.__grid.transform(self.__gui.bg_color(), f)
        self.__gui.clear()
        self.__gui.render()
        
        
    def map(self, func: function) -> None:
        ...
