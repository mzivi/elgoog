import collections
import heapq


def bfs(get_neighbors, source, target):
    """ Search a path from source to target with Breadth-First-Search. """

    parents = {}
    visited = set()
    queue = collections.deque()
    queue.append(source)
    while queue:
        vertex = queue.popleft()
        if vertex == target:
            return _backtrack(target, lambda v: parents.get(v))
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in filter(lambda n: n not in visited, get_neighbors(vertex)):
                queue.append(neighbor)
                parents[neighbor] = vertex
    return []


def dfs(get_neighbors, source, target):
    """ Search a path from source to target with Breadth-First-Search. """

    parents = {}
    visited = set()
    queue = collections.deque()
    queue.append(source)
    while queue:
        vertex = queue.pop()
        if vertex == target:
            return _backtrack(target, lambda v: parents.get(v))
        visited.add(vertex)
        neighbors = [n for n in get_neighbors(vertex) if n not in visited]
        if neighbors:
            queue.append(vertex)
            queue.append(neighbors[0])
            parents[neighbors[0]] = vertex
    return []


def dijkstra(get_neighbors, source, target, edge_weight):

    parents = {}
    visited = set()
    queue = []
    heapq.heappush(queue, (0.0, source, None))
    while queue:
        accrued, vertex, parent = heapq.heappop(queue)
        if vertex not in visited:
            visited.add(vertex)
            parents[vertex] = parent
            if vertex == target:
                return _backtrack(target, lambda v: parents.get(v))
            for neighbor in filter(lambda n: n not in visited, get_neighbors(vertex)):
                heapq.heappush(queue, (accrued + edge_weight(vertex, neighbor), neighbor, vertex))
    return []


def astar(get_neighbors, source, target, edge_weight, estimate_distance):

    parents = {}
    visited = {}
    queue = []
    heapq.heappush(queue, (estimate_distance(source, target), 0.0, source, None))
    while queue:
        estimated, accrued, vertex, parent = heapq.heappop(queue)
        if vertex not in visited:
            visited[vertex] = accrued
            parents[vertex] = parent
            if vertex == target:
                return _backtrack(target, lambda v: parents.get(v))
            for neighbor in filter(lambda n: n not in visited, get_neighbors(vertex)):
                new_accrued = accrued + edge_weight(vertex, neighbor)
                heapq.heappush(queue, (new_accrued + estimate_distance(neighbor, target), new_accrued, neighbor, vertex))
    return []


def _backtrack(vertex, get_parent):
    result = []
    while vertex:
        result.append(vertex)
        vertex = get_parent(vertex)
    result.reverse()
    return result


if __name__ == '__main__':

    agraph = {
        1: {2, 3},
        2: {1, 3, 5},
        3: {1, 2, 4, 6},
        4: {3, 5, 6},
        5: {2, 4},
        6: {3, 4}
    }
    print(' -> '.join(str(v) for v in bfs(lambda v: agraph[v], 1, 5)))
    print(' -> '.join(str(v) for v in dfs(lambda v: agraph[v], 1, 5)))

    weights = {}
    for n1, ns in agraph.items():
        for n2 in ns:
            weights[(n1, n2)] = 1.0
    weights[(2, 5)] = 10.
    weights[(3, 4)] = 10.
    print(' -> '.join(str(v) for v in dijkstra(lambda v: agraph[v], 1, 5, lambda v1, v2: weights[(v1, v2)])))

    import math

    graph_2d = {}
    weights_2d = {}
    side_len = 10
    for i in range(side_len + 1):
        for j in range(side_len + 1):
            graph_2d[(i, j)] = set()
            if i > 0:
                graph_2d[(i, j)].add((i - 1, j))
                weights_2d[((i, j), (i - 1, j))] = 1.0
                weights_2d[((i - 1, j), (i, j))] = 1.0
            if i < side_len:
                graph_2d[(i, j)].add((i + 1, j))
                weights_2d[((i, j), (i + 1, j))] = 1.0
                weights_2d[((i + 1, j), (i, j))] = 1.0
            if j > 0:
                graph_2d[(i, j)].add((i, j - 1))
                weights_2d[((i, j), (i, j - 1))] = 1.0
                weights_2d[((i, j - 1), (i, j))] = 1.0
            if j < side_len:
                graph_2d[(i, j)].add((i, j + 1))
                weights_2d[((i, j), (i, j + 1))] = 1.0
                weights_2d[((i, j + 1), (i, j))] = 1.0
            if i > 0 and j > 0:
                graph_2d[(i, j)].add((i - 1, j - 1))
                weights_2d[((i, j), (i - 1, j - 1))] = math.sqrt(2)
                weights_2d[((i - 1, j - 1), (i, j))] = math.sqrt(2)
            if i > 0 and j < side_len:
                graph_2d[(i, j)].add((i - 1, j + 1))
                weights_2d[((i, j), (i - 1, j + 1))] = math.sqrt(2)
                weights_2d[((i - 1, j + 1), (i, j))] = math.sqrt(2)
            if i < side_len and j > 0:
                graph_2d[(i, j)].add((i + 1, j - 1))
                weights_2d[((i, j), (i + 1, j - 1))] = math.sqrt(2)
                weights_2d[((i + 1, j - 1), (i, j))] = math.sqrt(2)
            if i < side_len and j < side_len:
                graph_2d[(i, j)].add((i + 1, j + 1))
                weights_2d[((i, j), (i + 1, j + 1))] = math.sqrt(2)
                weights_2d[((i + 1, j + 1), (i, j))] = math.sqrt(2)

    def estimate_cost(x, y):
        return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

    print(' -> '.join(str(v) for v in astar(
        lambda v: graph_2d[v], (0, 0), (side_len, side_len), lambda v1, v2: weights_2d[(v1, v2)], estimate_cost)))

    weights_2d[((4, 4), (5, 5))] = 100.0
    print(' -> '.join(str(v) for v in astar(
        lambda v: graph_2d[v], (0, 0), (side_len, side_len), lambda v1, v2: weights_2d[(v1, v2)], estimate_cost)))
    # (0, 0) -> (0, 1) -> (1, 2) -> (2, 3) -> (3, 4) -> (4, 5) -> (5, 5) -> (6, 6) -> (7, 7) -> (8, 8) -> (9, 9) -> (10, 10)
