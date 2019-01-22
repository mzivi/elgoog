import numpy as np
import numpy.random as random


def random_maze_on(nodes, neighbors_of):

    maze_map = {}
    node = nodes[random.choice(len(nodes))]
    from_node = {node: None}
    visited = {node}
    neighbors = neighbors_of(node)
    while neighbors:
        next_node = neighbors[random.choice(len(neighbors))]
        _link_undirected(node, next_node, maze_map)
        from_node[next_node] = node
        node = next_node
        visited.add(node)
        neighbors = [n for n in neighbors_of(node) if n not in visited]
        while not neighbors and from_node[node]:
            node = from_node[node]
            neighbors = [n for n in neighbors_of(node) if n not in visited]

    return lambda n: maze_map[n]


def _link_undirected(n1, n2, m):
    _link_to(n1, n2, m)
    _link_to(n2, n1, m)


def _link_to(n1, n2, m):
    if n1 not in m:
        m[n1] = {n2}
    else:
        m[n1].add(n2)


def get_neighbors_of(x, y, width, height):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < width - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < height - 1:
        neighbors.append((x, y + 1))
    return neighbors


def graph_from_grid(width, height):
    nodes = [(x, y) for x in range(width) for y in range(height)]
    return nodes, lambda n: get_neighbors_of(x=n[0], y=n[1], width=width, height=height)


def create_maze(width, height):
    # I use a matrix to represent the maze, where even rows and columns encode wall cells and odd rows and columns
    # encode corridor cells.
    # for wall cells: 0 = wall, 1 = no wall
    # for corridor cell: 0 = not visited, 1 = visited
    # The maze is complete when all corridor cells have been visited.
    grid = np.zeros((2 * width + 1, 2 * height + 1), dtype=int)

    # pick a random cell (or start from a specific one)
    x, y = random.randint(0, width), random.randint(0, height)
    from_cell = {(x, y): None}
    visit(x, y, grid)
    neighbors = get_neighbors_of(x, y, width, height)
    while neighbors:
        next_x, next_y = neighbors[random.choice(len(neighbors))]
        break_wall(x, y, next_x, next_y, grid)
        from_cell[(next_x, next_y)] = (x, y)
        x, y = next_x, next_y
        visit(x, y, grid)
        neighbors = [n for n in get_neighbors_of(x, y, width, height) if not already_visited(n, grid)]
        while not neighbors and from_cell[(x, y)]:
            (x, y) = from_cell[(x, y)]
            neighbors = [n for n in get_neighbors_of(x, y, width, height) if not already_visited(n, grid)]
    return grid


def visit(x, y, grid):
    grid[2 * x + 1, 2 * y + 1] = 1


def break_wall(from_x, from_y, next_x, next_y, grid):
    x = 2 * from_x + 1 + (next_x - from_x)
    y = 2 * from_y + 1 + (next_y - from_y)
    grid[x, y] = 1


def already_visited(neighbor, grid):
    x, y = neighbor
    return bool(grid[2 * x + 1, 2 * y + 1])


def render_grid_graph(width, height, neighbors_of, corridor_width=1):
    result = np.zeros((width * (corridor_width + 1) + 1, height * (corridor_width + 1) + 1), dtype=int)
    span = list(range(1, corridor_width + 1))
    for x in range(width):
        for y in range(height):
            for i in span:
                for j in span:
                    result[x * (corridor_width + 1) + i, y * (corridor_width + 1) + j] = 1
            for n in neighbors_of((x, y)):
                if x == n[0]:
                    for i in span:
                        result[x * (corridor_width + 1) + i, (y + n[1] + 1) * (corridor_width + 1) // 2] = 1
                if y == n[1]:
                    for i in span:
                        result[(x + n[0] + 1) * (corridor_width + 1) // 2, y * (corridor_width + 1) + i] = 1
    return result


if __name__ == '__main__':
    nodes, neighbors_of = graph_from_grid(25, 25)
    maze_neighbors_of = random_maze_on(nodes, neighbors_of)
    rendered_maze = render_grid_graph(25, 25, maze_neighbors_of, corridor_width=1)

    import matplotlib.pyplot as plt
    import matplotlib.colors as colors

    plt.axis('off')
    cmap = colors.ListedColormap(np.array([[0, 0, 0], [1, 1, 1]]))
    plt.imshow(rendered_maze, cmap=cmap)
    pass
