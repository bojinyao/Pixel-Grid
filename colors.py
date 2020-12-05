from collections import namedtuple


class Color(namedtuple('Color', ['r', 'g', 'b'])):

    def __new__(cls, *args: int) -> None:
        if len(args) == 1:
            assert 0 <= args[0] <= 255, 'RGB must be between 0 and 255'
            assert type(args[0]) is int, 'input must be an int between 0 and 255'
            r = g = b = args[0]
            return super().__new__(cls, r, g, b)
        elif len(args) == 3:
            for i, c in enumerate(args):
                assert 0 <= c <= 255, f'{i}: {c} must be between 0 and 255'
                assert type(c) is int, f'{i}: {c} must be an int between 0 and 255'
            return super().__new__(cls, args[0], args[1], args[2])
        else:
            raise ValueError(f'1 or 3 arguments expected, got {len(args)}')

    def __repr__(self) -> str:
        return f'({self.r}, {self.g}, {self.b})'


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
