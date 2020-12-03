from typing import Iterator
from point import Point

from collections.abc import Collection
from itertools import chain, product
from pprint import pformat


class Grid(Collection):

    def __init__(self, height: int, width: int = None, fill: object = None) -> None:
        if not width:
            width = height
        self.__height = height
        self.__width = width
        self.__fill = fill
        self.grid = [[fill for _ in range(
            width)] for _ in range(height)]

    def __getitem__(self, p: Point) -> object:
        return self.grid[p.y][p.x]

    def __setitem__(self, p: Point, c: object) -> None:
        self.grid[p.y][p.x] = c

    def __contains__(self, o: object) -> bool:
        for y, x in product(range(self.__height), range(self.__width)):
            if self.grid[y][x] == o:
                return True
        return False

    def __iter__(self) -> Iterator[object]:
        for (y, x), o in zip(product(range(self.__height), range(self.__width)), chain.from_iterable(self.grid)):
            # this unfortunate hack to reverse order of y, and x
            yield (x, y), o

    def __len__(self) -> int:
        return self.__width * self.__height

    def __str__(self) -> str:
        return pformat(self.grid, width=200)

    def fill(self, o: object) -> None:
        for y, x in product(range(self.__height), range(self.__width)):
            self.grid[y][x] = o

    def refill(self) -> None:
        self.fill(self.__fill)

    def width(self) -> int:
        return self.__width

    def height(self) -> int:
        return self.__height
