# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and
# return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6


class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        length = [[0] * m for _ in range(n)]
        for i in range(n):
            length[i][0] = 0 if matrix[i][0] == '0' else 1
            for j in range(1, m):
                length[i][j] = 0 if matrix[i][j] == '0' else 1 + length[i][j - 1]
        max_area = max(length[0])
        for i in range(1, n):
            for j in range(m):
                max_len = length[i][j]
                max_area = max(max_area, max_len)
                k = 1
                while k < i + 1 and length[i - k][j] > 0:
                    max_len = min(max_len, length[i - k][j])
                    k += 1
                    max_area = max(max_area, max_len * k)
        return max_area


if __name__ == '__main__':

    result = Solution().maximalRectangle([['0', '1']])
    assert result == 1
    result = Solution().maximalRectangle([['1']])
    assert result == 1
    result = Solution().maximalRectangle(
        [
          ["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]
        ])
    assert result == 6
