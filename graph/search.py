from collections import namedtuple
from collections import deque
import heapq
from functools import partial


def calculate_path_cost(graph, path):
    cost = 0
    if len(path) > 1:
        for i in range(1, len(path)):
            cost += graph[path[i - 1]][path[i]]
    return cost


def find_path(graph, source=0, target=0, strategy="BFS"):

    _validate(graph)

    n = len(graph)
    if source < 0 or source >= n:
        raise Exception("invalid source {}: it should be in [0, {})".format(source, n))
    if target < 0 or target >= n:
        raise Exception("invalid target {}: it should be in [0, {})".format(target, n))

    if strategy == "BFS":
        result = _breath_first_search(graph, source, target)
    elif strategy == "dijkstra":
        result = _dijkstra(graph, source, target)
    else:
        raise Exception("Unknown strategy: {}".format(strategy))

    return result


def _validate(graph):
    n = len(graph)
    for i, row in enumerate(graph):
        if len(row) != n:
            raise Exception("Invalid graph: row {} has {} elements while it should have {}.".format(i, len(row), n))


def _breath_first_search(graph, source, target):
    # nodes are enriched with a field which represent the node they come from to backtrack the shortest path
    Node = namedtuple('Node', ['element', 'origin'])
    nodes_queue = deque()
    nodes_queue.appendleft(Node(source, None))
    visited = set()
    while nodes_queue:
        next_node = nodes_queue.pop()
        node_index, origin = next_node
        visited.add(node_index)
        if node_index == target:
            return _backtrack(next_node)
        for i, weight in enumerate(graph[node_index]):
            if i not in visited and weight:
                nodes_queue.appendleft(Node(i, next_node))
    return []


def _backtrack(node):
    result = [node.element]
    while node.origin:
        node = node.origin
        result.append(node.element)
    result.reverse()
    return result


class DNode:
    def __init__(self, element, origin, cost):
        self.element = element
        self.origin = origin
        self.cost = cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __ge__(self, other):
        return self.cost >= other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __len__(self):
        return 3

    def __iter__(self):
        return iter((self.element, self.origin, self.cost))


def _dijkstra(graph, source, target):
    nodes_queue = []
    heapq.heappush(nodes_queue, DNode(source, None, 0))
    visited = set()
    while nodes_queue:
        next_node = heapq.heappop(nodes_queue)
        node_index, origin, cost = next_node
        visited.add(node_index)
        if node_index == target:
            return _backtrack(next_node)
        for i, weight in enumerate(graph[node_index]):
            if i not in visited and weight:
                heapq.heappush(nodes_queue, DNode(i, next_node, cost + weight))
    return []


class ANode:
    def __init__(self, element, origin, cost_accrued, estimated_cost):
        self.element = element
        self.origin = origin
        self.cost_accrued = cost_accrued
        self.estimated_cost = estimated_cost

    @property
    def total_est_cost(self):
        return self.cost_accrued + self.estimated_cost

    def __le__(self, other):
        return self.total_est_cost <= other.total_est_cost

    def __lt__(self, other):
        return self.total_est_cost < other.total_est_cost

    def __ge__(self, other):
        return self.total_est_cost >= other.total_est_cost

    def __gt__(self, other):
        return self.total_est_cost > other.total_est_cost

    def __len__(self):
        return 4

    def __iter__(self):
        return iter((self.element, self.origin, self.cost_accrued, self.estimated_cost))


def astar(source, target, estimate_cost_fun, get_neighbors_fun):
    nodes_queue = []
    heapq.heappush(nodes_queue, ANode(source, None, 0, estimate_cost_fun(source, target)))
    visited = set()
    while nodes_queue:
        next_node = heapq.heappop(nodes_queue)
        element, origin, cost_accrued, estimated_cost = next_node
        if element not in visited:
            visited.add(element)
            if element == target:
                return _backtrack(next_node)
            for neighbor, weight in get_neighbors_fun(element):
                if neighbor not in visited and weight:
                    heapq.heappush(nodes_queue, ANode(neighbor, next_node, cost_accrued + weight, estimate_cost_fun(neighbor, target)))
    return []


if __name__ == "__main__":

    def run_path_finder(graph, source, target, strategy):
        path = find_path(graph, source, target, strategy=strategy)
        return source, target, calculate_path_cost(graph, path), path

    agraph = [[None, 0.2, 0.8], [None, None, 0.2], [None, None, None]]

    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 0, 'BFS')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 1, 'BFS')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 2, 'BFS')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 1, 2, 'BFS')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 1, 0, 'BFS')))

    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 0, 'dijkstra')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 1, 'dijkstra')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 2, 'dijkstra')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 1, 2, 'dijkstra')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 1, 0, 'dijkstra')))

    # this graph has a loop
    agraph = [
        [None, 1, 0.2, None, None, None],
        [None, None, None, 0.2, None, None],
        [None, 0.2, None, None, None, None],
        [None, None, None, None, 0.2, 1],
        [None, None, 1, None, None, 0.2],
        [None, None, None, None, None, None]
    ]
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 5, 'BFS')))
    print("from {} to {} costs {}: {}".format(*run_path_finder(agraph, 0, 5, 'dijkstra')))

    import math

    graph_2d = {}
    side_len = 10
    for i in range(side_len + 1):
        for j in range(side_len + 1):
            graph_2d[(i, j)] = {}
            if i > 0:
                graph_2d[(i, j)][(i - 1, j)] = 1.0
            if i < side_len:
                graph_2d[(i, j)][(i + 1, j)] = 1.0
            if j > 0:
                graph_2d[(i, j)][(i, j - 1)] = 1.0
            if j < side_len:
                graph_2d[(i, j)][(i, j + 1)] = 1.0
            if i > 0 and j > 0:
                graph_2d[(i, j)][(i - 1, j - 1)] = math.sqrt(2)
            if i > 0 and j < side_len:
                graph_2d[(i, j)][(i - 1, j + 1)] = math.sqrt(2)
            if i < side_len and j > 0:
                graph_2d[(i, j)][(i + 1, j - 1)] = math.sqrt(2)
            if i < side_len and j < side_len:
                graph_2d[(i, j)][(i + 1, j + 1)] = math.sqrt(2)

    def estimate_cost(x, y):
        return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


    def get_neighbors(element, graph):
        return graph[element].items()

    def run_astar(graph, source, target):
        path = astar(source, target, estimate_cost, partial(get_neighbors, graph=graph))
        return source, target, calculate_path_cost(graph, path), path

    print("from {} to {} costs {}: {}".format(*run_astar(graph_2d, (0, 0), (side_len, side_len))))

    graph_2d[(4, 4)][(5, 5)] = None
    print("from {} to {} costs {} (with block from (4, 4) to (5, 5)): {}".format(*run_astar(graph_2d, (0, 0), (side_len, side_len))))
