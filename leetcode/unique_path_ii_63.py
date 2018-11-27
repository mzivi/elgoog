# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if obstacleGrid[0][0] == 1:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    result = [[1]]
    for j in range(1, n):
        result[0].append(1 if obstacleGrid[0][j] == 0 and result[0][j-1] > 0 else 0)
    for i in range(1, m):
        row_i = [1 if obstacleGrid[i][0] == 0 and result[i-1][0] > 0 else 0]
        result.append(row_i)
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                row_i.append(0)
            else:
                row_i.append(row_i[-1] + result[i-1][j])
    return result[-1][-1]


if __name__ == '__main__':

    print(uniquePathsWithObstacles([[1]]))
    print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
