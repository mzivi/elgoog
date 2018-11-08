from collections import deque
from collections import namedtuple


def find_path(graph, source=0, target=0, strategy="BFS"):

    _validate(graph)

    n = len(graph)
    if source < 0 or source >= n:
        raise Exception("invalid source {}: it should be in [0, {})".format(source, n))
    if target < 0 or target >= n:
        raise Exception("invalid target {}: it should be in [0, {})".format(target, n))

    if strategy == "BFS":
        result = _breath_first_search(graph, source, target)
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
    nodes_queue.appendleft(Node(source, origin=None))
    visited = set()
    while nodes_queue:
        next_node = nodes_queue.pop()
        node_index, origin = next_node
        visited.add(node_index)
        if node_index == target:
            return _backtrack(next_node)
        for i, weight in enumerate(graph[node_index]):
            if i not in visited and weight > 0:
                nodes_queue.appendleft(Node(i, next_node))
    return []


def _backtrack(node):
    result = [node.index]
    while node.origin:
        node = node.origin
        result.append(node.index)
    result.reverse()
    return result


if __name__ == "__main__":
    agraph = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]

    def run_search(graph, source, target, strategy):
        return source, target, find_path(agraph, source, target, strategy)

    print("from {} to {}: {}".format(*run_search(agraph, 0, 0, strategy="BFS")))
    print("from {} to {}: {}".format(*run_search(agraph, 0, 1, strategy="BFS")))
    print("from {} to {}: {}".format(*run_search(agraph, 0, 2, strategy="BFS")))
    print("from {} to {}: {}".format(*run_search(agraph, 1, 2, strategy="BFS")))
    print("from {} to {}: {}".format(*run_search(agraph, 1, 0, strategy="BFS")))
