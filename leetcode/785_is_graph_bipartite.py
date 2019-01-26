# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B
# such that every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes
# i and j exists.Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges:
# graph[i] does not contain i, and it doesn 't contain any element twice.
#
# Example
# 1:
# Input: [[1, 3], [0, 2], [1, 3], [0, 2]]
# Output: true
# Explanation:
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
# Example 2:
# Input: [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
# Output: false
# Explanation:
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.
#
# Note:
#
# graph will have length in range[1, 100].
# graph[i] will contain integers in range[0, graph.length - 1].
# graph[i] will not contain i or duplicate values.
# The graph is undirected:
# if any element j is in graph[i], then i will be in graph[j].

from collections import deque

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        A = set()
        B = set()
        A.add(0)
        queue = deque()
        queue.append(0)
        visited = set()
        while queue or len(A | B) < len(graph):
            n1 = queue.pop() if queue else list(filter(lambda n: n not in A | B, range(len(graph))))[0]
            if len(graph[n1]) == 0:
                A.add(n1)
            this_set = A if n1 in A else B
            other_set = B if n1 in A else A
            for n2 in graph[n1]:
                if n2 in this_set:
                    return False
                other_set.add(n2)
                if n2 not in visited:
                    queue.append(n2)
            visited.add(n1)
        return True


if __name__ == '__main__':

    result = Solution().isBipartite(
        [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],
         [20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],
         [40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]])
    assert not result
    result = Solution().isBipartite(
        [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
         [2, 4, 5, 6, 7, 8]])
    assert not result
    result = Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]])
    assert result
    result = Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])
    assert not result
