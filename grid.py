from typing import Iterator
from colors import Color, BLACK
from point import Point

from collections.abc import Collection
from itertools import chain
from pprint import pformat


class Grid(Collection):

    def __init__(self, height: int, width: int = None, default_color: Color = BLACK) -> None:
        if not width:
            width = height
        self.__height = height
        self.__width = width
        self.grid = [[default_color for _ in range(
            width)] for _ in range(height)]

    def __getitem__(self, p: Point) -> Color:
        return self.grid[p.y][p.x]

    def __setitem__(self, p: Point, c: Color) -> None:
        self.grid[p.y][p.x] = c

    def __contains__(self, c: Color) -> bool:
        for y in range(self.__height):
            for x in range(self.__width):
                if self.grid[y][x] == c:
                    return True
        return False

    def __iter__(self) -> Iterator[Point]:
        return chain.from_iterable(self.grid)

    def __len__(self) -> int:
        return self.__width * self.__height

    def __str__(self) -> str:
        return pformat(self.grid, width=200)

    def width(self) -> int:
        return self.__width

    def height(self) -> int:
        return self.__height
