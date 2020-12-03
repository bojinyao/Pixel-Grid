from grid import Grid
from gui import GUI

"""Main file

This also acts as the controller of the app
"""

__DEFAULT_W_HEIGHT = 600
__DEFAULT_W_WIDTH = 600


class Gridviz:
    
    def __init__(self, height: int, width: int = None, window_height: int = __DEFAULT_W_HEIGHT, window_width: int = __DEFAULT_W_WIDTH) -> None:        
        self.__grid = Grid(height, width)
        self.__gui = GUI(self.__grid, window_height, window_width)
        
