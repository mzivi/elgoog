# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
#  range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed
# integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        max_i = str(2**31 - 1)
        min_i = str(-2**31)
        s = ''.join(reversed(str(abs(x))))
        if x < 0:
            s = '-' + s
            # let's compare before casting back to int and leverage on lexicographic comparison
            if len(s) > len(min_i) or (len(s) == len(min_i) and s > min_i):
                return 0
        else:
            # let's compare before casting back to int and leverage on lexicographic comparison
            if len(s) > len(max_i) or (len(s) == len(max_i) and s > max_i):
                return 0
        return int(s)


if __name__ == '__main__':

    result = Solution().reverse(-2147483412)
    assert result == -2143847412
    result = Solution().reverse(1534236469)
    assert result == 0
    result = Solution().reverse(123)
    assert result == 321
    result = Solution().reverse(-123)
    assert result == -321
    result = Solution().reverse(120)
    assert result == 21
