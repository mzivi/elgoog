# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
from itertools import cycle

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) <= numRows:
            return s

        result = ""
        for i in range(numRows):
            if i >= len(s):
                return result
            step_1 = 2 * (numRows - i - 1) if i < numRows - 1 else 2 * i
            step_2 = 2 * i if i > 0 else 2 * (numRows - i - 1)
            next_i = i
            for step in cycle([step_1, step_2]):
                result += s[next_i]
                next_i += step
                if next_i >= len(s):
                    break
        return result


if __name__ == '__main__':

    result = Solution().convert("A", 1)
    assert result == "A"
    result = Solution().convert("PAYPALISHIRING", 3)
    assert result == "PAHNAPLSIIGYIR"
    result = Solution().convert("PAYPALISHIRING", 4)
    assert result == "PINALSIGYAHRPI"
