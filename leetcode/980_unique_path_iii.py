# On a 2-dimensional grid, there are 4 types of squares:
#  1. represents the starting square.There is exactly one starting square.
#  2. represents the ending square.There is exactly one ending square.
#  0. represents empty squares we can walk over.
#  -1. represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every
# non - obstacle square exactly once.
#
# Example 1:
#
# Input: [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
# Output: 2
# Explanation: We have the following two paths:
# 1.(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)
# 2.(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2)
# Example 2:
#
# Input: [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
# Output: 4
# Explanation: We have the following four paths:
# 1.(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)
# 2.(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3)
# 3.(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)
# 4.(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2), (2, 3)
# Example 3:
#
# Input: [[0, 1], [2, 0]]
# Output: 0
# Explanation:
# There is no path that walks over every empty square exactly once. Note that the starting and ending square can be
# anywhere in the grid.
#
# Note:
#
# 1 <= grid.length * grid[0].length <= 2
import collections


class Solution:

    def uniquePathsIII(self, grid: 'List[List[int]]') -> 'int':
        n = len(grid)
        m = len(grid[0])
        visited = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    visited[(i, j)] = 0
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    stop = (i, j)

        def neighbors_of(x):
            return filter(
                lambda y: 0 <= y[0] < n and 0 <= y[1] < m and grid[y[0]][y[1]] in [0, 2],
                ((x[0] - 1, x[1]), (x[0], x[1] + 1), (x[0] + 1, x[1]), (x[0], x[1] - 1)))

        return self.count_paths(neighbors_of, start, stop, visited, 0)

    def count_paths(self, neighbors_of, start, stop, visited, nvisited):
        npaths = 0
        for x in neighbors_of(start):
            if x == stop:
                npaths += 1 if len(visited) == nvisited else 0
            # then is a walkable cell (see neighbors_of above)
            elif visited[x] == 0:  # not visited yet
                visited[x] = 1
                npaths += self.count_paths(neighbors_of, x, stop, visited, nvisited + 1)
                visited[x] = 0
        return npaths


if __name__ == "__main__":

    result = Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    assert result == 2
    result = Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
    assert result == 4
    result = Solution().uniquePathsIII([[0,1],[2,0]])
    assert result == 0
