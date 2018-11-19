import numpy.random as rnd
import math
from graph.search import astar


def generate_problem(size=4, avg_steps=100):
    problem = solution_for(size)
    while rnd.randint(0, avg_steps) > 0:
        neighbors = _get_neighbors(problem)
        problem = neighbors[rnd.choice(len(neighbors))]
    return problem


def solution_for(size=4):
    numbers = list(range(1, size * size))
    numbers.append(None)
    return tuple(numbers)


def calculate_distance(c1, c2):
    if len(c2) != len(c2):
        raise Exception('Non-conformant times: len(c1) = {} and len(c2) = {}'.format(len(c1), len(c2)))
    size = len(c1)
    side_len = int(round(math.sqrt(size)))
    if side_len * side_len != size:
        raise Exception('tiles are not square: {}, {}'.format(c1, c2))
    distance = 0
    for i in range(size):
        if c1[i] is not None:
            x1, y1 = _index_coordinates(i, side_len)
            x2, y2 = _index_coordinates(c2.index(c1[i]), side_len)
            distance += abs(x2 - x1) + abs(y2 - y1)
    return distance


def _index_coordinates(i, side_len):
    return i % side_len, i // side_len


def _coordinates_index(x, y, side_len):
    return y * side_len + x


def _get_neighbors(tiles):
    side_len = int(round(math.sqrt(len(tiles))))
    i_none = tiles.index(None)
    x, y = _index_coordinates(i_none, side_len)
    neighbors = []
    if x > 0:
        new_tiles = list(tiles)
        i = _coordinates_index(x - 1, y, side_len)
        new_tiles[i_none], new_tiles[i] = new_tiles[i], new_tiles[i_none]
        neighbors.append(tuple(new_tiles))
    if x < side_len - 1:
        new_tiles = list(tiles)
        i = _coordinates_index(x + 1, y, side_len)
        new_tiles[i_none], new_tiles[i] = new_tiles[i], new_tiles[i_none]
        neighbors.append(tuple(new_tiles))
    if y > 0:
        new_tiles = list(tiles)
        i = _coordinates_index(x, y - 1, side_len)
        new_tiles[i_none], new_tiles[i] = new_tiles[i], new_tiles[i_none]
        neighbors.append(tuple(new_tiles))
    if y < side_len - 1:
        new_tiles = list(tiles)
        i = _coordinates_index(x, y + 1, side_len)
        new_tiles[i_none], new_tiles[i] = new_tiles[i], new_tiles[i_none]
        neighbors.append(tuple(new_tiles))
    return neighbors


def _get_neighbors_with_unit_weights(tiles):
    return [(neighbor, 1.0) for neighbor in _get_neighbors(tiles)]


def solve(problem):
    side_len = int(round(math.sqrt(len(problem))))
    solved = solution_for(side_len)
    return astar(problem, solved, calculate_distance, _get_neighbors_with_unit_weights)


if __name__ == "__main__":

    problem = (1, 2, 3, 5, 7, 6, 4, 8, None)
    print(problem)
    print(solve(problem))

    problem = generate_problem()
    print(problem)
    print(solve(problem))
