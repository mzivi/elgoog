# generate a maze

import random
from collections import Deque


def generate_mase(m, n):
    maze = init_maze()
    i, j = 0, 0
    while (i, j) != (m - 1, n - 1):
        open_cell(maze[i][j])
        i, j = find_closest(maze, i, j)
    return maze


def _init_maze(m, n)
    maze = [[sample_cell() for j in range(n)] for i in range(m)]


def sample_cell():
    return [random.randomint(2) for _ in range(4)]


def find_closest(maze, x, y):
    finish_x = len(maze) - 1
    finish_y = len(maze[0]) - 1
    visited = set()
    queue = Deque()
    queue.appendleft((x, y))
    while queue:
        i, j = queue.pop()
        if (i, j) = (finish_x, finish_y):
            return (i, j)
        cell = maze[i][j]
        for k in range(4):
            if cell[k] and


def open_cell(cell):
    for i in range(len(cell)):
        if cell[i] = 0:
            cell[i] = 1
