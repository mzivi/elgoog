# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    gridsum = [[grid[0][0]]]
    for j in range(1, n):
        gridsum[0].append(gridsum[0][j-1] + grid[0][j])
    for i in range(1, m):
        rowsum = [gridsum[i-1][0] + grid[i][0]]
        gridsum.append(rowsum)
        for j in range(1, n):
            rowsum.append(min([rowsum[j-1], gridsum[i-1][j]]) + grid[i][j])
    return gridsum[-1][-1]


if __name__ == '__main__':
    print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
