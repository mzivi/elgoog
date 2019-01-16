import numpy as np
from graph.search import astar
import maze


def draw_path(path, maze):
    result = np.copy(maze)
    for cell in path:
        result[2 * cell[0] + 1, 2 * cell[1] + 1] = 2
    return result


def on_path(x, y, grid):
    if 0 < x < grid.shape[0] - 1:
        if grid[x - 1, y] > 1 and grid[x + 1, y] > 1:
            return True
    if 0 < y < grid.shape[1] - 1:
        if grid[x, y - 1] > 1 and grid[x, y + 1] > 1:
            return True
    return False


def rendering_grid(grid, corridor_width):
    width = grid.shape[0] // 2
    height = grid.shape[1] // 2
    result = np.ones((width * (corridor_width + 1) + 1, height * (corridor_width + 1) + 1), dtype=int)
    long_span = list(range(1, corridor_width + 1))
    short_span = [0]
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            x_is_odd = bool(x % 2)
            y_is_odd = bool(y % 2)
            if x_is_odd and y_is_odd:  # it's a corridor cell
                if grid[x, y] > 1:
                    for i in long_span:
                        for j in long_span:
                            result[(x // 2) * (corridor_width + 1) + i, (y // 2) * (corridor_width + 1) + j] = grid[x, y]
                continue

            render_with = 0
            if grid[x, y] > 0:  # there is no wall here
                if not on_path(x, y, grid):
                    continue
                # this is on the solution path
                render_with = 2
            span_x = long_span if x_is_odd else short_span
            span_y = long_span if y_is_odd else short_span
            for i in span_x:
                for j in span_y:
                    result[(x // 2) * (corridor_width + 1) + i, (y // 2) * (corridor_width + 1) + j] = render_with
    return result


def estimate_cost_fun(source, target):
    return abs(source[0] - target[0]) + abs(source[1] - target[1])


def no_wall_between(cell1, cell2):
    x = cell1[0] + cell2[0] + 1
    y = cell1[1] + cell2[1] + 1
    return amaze[x, y] == 1


def get_neighbors_fun(cell):
    return [(n, 1.) for n in maze.get_neighbors_of(cell[0], cell[1], width, height) if no_wall_between(cell, n)]


if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import matplotlib.colors as colors

    width, height = 20, 20
    maze_id = 12
    amaze = maze.create_maze(width, height)

    # open entry and exit points
    amaze[:2, :2] = 1
    amaze[-2:, -2:] = 1
    # mark entry and exit cells
    amaze[1, 1] = 3
    amaze[-2, -2] = 4
    rendered_maze = rendering_grid(amaze, 4)
    plt.axis('off')
    cmap = colors.ListedColormap(np.array([[0, 0, 0], [1, 1, 1], [0, 0, 1], [1, 0, 0], [0, 1, 0]]))
    plt.imshow(rendered_maze, cmap=cmap)
    plt.savefig('mazes/maze_{}.png'.format(maze_id), bbox_inches='tight', pad_inches=0, dpi=300)

    path = astar((0, 0), (width - 1, height - 1), estimate_cost_fun, get_neighbors_fun)
    solved_maze = draw_path(path, amaze)
    solved_maze[1, 1] = 3
    solved_maze[-2, -2] = 4

    rendered_solved_maze = rendering_grid(solved_maze, 4)

    plt.figure()
    plt.axis('off')
    cmap = colors.ListedColormap(np.array([[0, 0, 0], [1, 1, 1], [0, 0, 1], [1, 0, 0], [0, 1, 0]]))
    plt.imshow(rendered_solved_maze, cmap=cmap)
    plt.savefig('mazes/solved_maze_{}.png'.format(maze_id), bbox_inches='tight', pad_inches=0, dpi=300)
