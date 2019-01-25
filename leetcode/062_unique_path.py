# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    results = [[1] * n]
    for i in range(1, m):
        results += [[1]]
        for j in range(1, n):
            results[i].append(results[i][j - 1] + results[i - 1][j])
    return results[-1][-1]


if __name__ == '__main__':

    print(uniquePaths(3, 3))
    print(uniquePaths(3, 2))
