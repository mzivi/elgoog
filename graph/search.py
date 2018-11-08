from collections import namedtuple
from collections import deque
import heapq


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
    Node = namedtuple('Node', ['index', 'origin'])
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
    result = [node.index]
    while node.origin:
        node = node.origin
        result.append(node.index)
    result.reverse()
    return result


class DNode:
    def __init__(self, index, origin, cost):
        self.index = index
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
        return iter((self.index, self.origin, self.cost))


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


if __name__ == "__main__":
    agraph = [[None, 0.2, 0.8], [None, None, 0.2], [None, None, None]]

    def run_path_finder(graph, source, target, strategy):
        path = find_path(graph, source, target, strategy=strategy)
        return source, target, calculate_path_cost(graph, path), path

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
