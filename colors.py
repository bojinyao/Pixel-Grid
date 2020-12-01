from collections import namedtuple


class Color(namedtuple('Color', ['r', 'g', 'b'])):

    def __repr__(self) -> str:
        return f'({self.r}, {self.g}, {self.b})'


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
