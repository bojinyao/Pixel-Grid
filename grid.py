from typing import Iterator, Callable
from point import Point

from collections.abc import Collection
from itertools import chain, product
from pprint import pformat
from copy import deepcopy
from math import sqrt


class Grid(Collection):

    def __init__(self, height: int, width: int = None, fill: object = None) -> None:
        if not width:
            width = height
        self.__height = height
        self.__width = width
        self.__fill = fill
        self.__grid = [[fill for _ in range(
            width)] for _ in range(height)]

    def __getitem__(self, p: Point) -> object:
        return self.__grid[p.y][p.x]

    def __setitem__(self, p: Point, c: object) -> None:
        self.__grid[p.y][p.x] = c

    def __contains__(self, o: object) -> bool:
        for y, x in product(range(self.__height), range(self.__width)):
            if self.__grid[y][x] == o:
                return True
        return False

    def __iter__(self) -> Iterator[tuple[tuple[int, int], object]]:
        for (y, x), o in zip(product(range(self.__height), range(self.__width)), chain.from_iterable(self.__grid)):
            # this unfortunate hack to reverse order of y, and x
            yield (x, y), o

    def __len__(self) -> int:
        return self.__width * self.__height

    def __str__(self) -> str:
        return pformat(self.__grid, width=200)

    def fill(self, o: object) -> None:
        for y, x in product(range(self.__height), range(self.__width)):
            self.__grid[y][x] = o

    def refill(self) -> None:
        self.fill(self.__fill)

    def resize(self, new_height: int, new_width: int) -> None:
        grid = [[self.__fill for _ in range(new_width)] for _ in range(new_height)]
        for y, x in product(range(min(self.__height, new_height)), range(min(self.__width, new_width))):
            grid[y][x] = self.__grid[y][x]
        self.__grid = grid
        self.__width = new_width
        self.__height = new_height

    def transform(self, discard_val: object, func: Callable[[int, int, object], bool]) -> None:
        """Run filter using an input function

        Args:
            func (function[[int, int, object], bool]): A function that takes in 3 arguments, x, y coordinates and object
        """
        for (x, y), o in self.__iter__():
            if not func(x, y, o):
                self.__grid[y][x] = discard_val
                
    def apply(self, func: Callable[[int, int, object], object]) -> None:
        """Run map using an input function

        Args:
            func (function[[int, int, object], object]): A function that takes in 3 arguments, x, y coordinates and object
        """
        for (x, y), o in self.__iter__():
            self.__grid[y][x] = func(x, y, o)
            
            
    def scale_up(self, replacements: dict[object, object]) -> None:
        old_width = self.__width
        old_height = self.__height
        old_list = self.grid_list()
        new_width = self.__width ** 2
        new_height = self.__height ** 2
        self.resize(new_height, new_width)
        for y, x in product(range(old_height), range(old_width)):
            if old_list[y][x] in replacements:
                content = replacements[old_list[y][x]]
                for j, i in product(range(old_height), range(old_width)):
                    self.__grid[j + y * old_height][i + x * old_width] = content
            else:
                for j, i in product(range(old_height), range(old_width)):
                    self.__grid[j + y * old_height][i + x * old_width] = old_list[j][i]
            
            
    def scale_down(self) -> bool:
        old_width = self.__width
        old_height = self.__height
        new_width = sqrt(old_width)
        new_height = sqrt(old_height)
        if not (new_width == int(new_width) and new_height == int(new_height)):
            return False
        self.resize(int(new_height), int(new_width))
        return True

    def grid_list(self) -> list[list[object]]:
        """Return a deepcopy of underlying list of lists

        Returns:
            list[list[object]]: a deepcopy of underlying grid
        """
        return deepcopy(self.__grid)

    def width(self) -> int:
        return self.__width

    def height(self) -> int:
        return self.__height
