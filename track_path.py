import gui
import grid
from gridviz import Viz
from colors import BLACK, Color, WHITE
import time

if __name__ == "__main__":
    viz = Viz(3)
    grid = \
    [['player', 'path', 'path', 'path', 'path'],
    ['path', 'wall', 'wall', 'wall', 'wall'],
    ['path', 'wall', 'path', 'path', 'path'],
    ['path', 'wall', 'wall', 'wall', 'path'],
    ['path', 'path', 'path', 'path', 'target']]
    mapping = {'path': 'white', 'wall': 'black', 'player': 'red', 'target': 'green'}
    path = [[1,0, 0,0], [2,0, 1,0], [3,0, 2,0], [4,0, 3,0], [4,1, 4,0], [4,2, 4,1], [4,3, 4,2], [4,4, 4,3]]
    viz.track(grid, mapping)

    for move in path:
        time.sleep(1)
        grid[move[0]][move[1]] = 'player'
        grid[move[2]][move[3]] = 'path'
        viz.update()
    time.sleep(5)
