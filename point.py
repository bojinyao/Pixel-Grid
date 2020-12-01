from collections import namedtuple


class Point(namedtuple('Point', ['x', 'y'])):

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
