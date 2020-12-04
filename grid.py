from typing import Iterator
from point import Point

from collections.abc import Collection
from itertools import chain, product
from pprint import pformat
from copy import deepcopy


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

    def resize(self, newHeight: int, newWidth: int) -> None:
        grid = [[self.__fill for _ in range(newWidth)] for _ in range(newHeight)]
        for y, x in product(range(min(self.__height, newHeight)), range(min(self.__width, newWidth))):
            grid[y][x] = self.__grid[y][x]
        self.__grid = grid
        self.__width = newWidth
        self.__height = newHeight

    def transform(self, discard_val: object, func: function[[int, int, object], bool]) -> None:
        """Run filter using an input function

        Args:
            func (function[[int, int, object], bool]): A function that takes in 3 arguments, x, y coordinates and object
        """
        for (x, y), o in self.__iter__():
            if not func(x, y, o):
                self.__grid[y][x] = discard_val
                
    def apply(self, func: function[[int, int, object], object]) -> None:
        """Run map using an input function

        Args:
            func (function[[int, int, object], object]): A function that takes in 3 arguments, x, y coordinates and object
        """
        for (x, y), o in self.__iter__():
            self.__grid[y][x] = func(x, y, o)
            

    def grid(self) -> list[list[object]]:
        """Return a deepcopy of underlying list of lists

        Returns:
            list[list[object]]: a deepcopy of underlying grid
        """
        return deepcopy(self.__grid)

    def width(self) -> int:
        return self.__width

    def height(self) -> int:
        return self.__height
