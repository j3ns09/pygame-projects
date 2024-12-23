from random import random

class Spot:
    def __init__(self, i, j):
        self.i = i
        self.j = j

        self.f = 0.
        self.g = 0.
        self.h = 0.

        self.neighbours : list[Spot] = []
        self.previous : None | Spot = None
        self.is_wall = random() < .35

    def add_neighbours(self, grid):
        i, j = self.i, self.j
        n = len(grid)
        n_i = len(grid[0])
        if j < n - 1:
            self.neighbours.append(grid[j + 1, i])
        if j > 0:
            self.neighbours.append(grid[j - 1, i])
        if i < n_i - 1:
            self.neighbours.append(grid[j, i + 1])
        if i > 0:
            self.neighbours.append(grid[j, i - 1])

        if i > 0 and j > 0:
            self.neighbours.append(grid[j - 1, i - 1])
        if i > 0 and j < n - 1:
            self.neighbours.append(grid[j + 1, i - 1])
        if i < n_i - 1 and j > 0:
            self.neighbours.append(grid[j - 1, i + 1])
        if (i < n_i - 1) and (j < n - 1):
            self.neighbours.append(grid[j + 1, i + 1])

    def __repr__(self):
        return f"Spot(x={self.i}, y={self.j})"
