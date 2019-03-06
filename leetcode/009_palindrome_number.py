# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?


class Solution:

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        s1 = 0
        while s1 < x:
            s1 = s1 * 10 + x % 10
            x = x // 10
        return s1 == x or s1 // 10 == x


    def isPalindrome_str(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == ''.join(reversed(str(x)))


if __name__ == "__main__":

    result = Solution().isPalindrome(1221)
    assert result
    result = Solution().isPalindrome(121)
    assert result
    result = Solution().isPalindrome(-121)
    assert not result
    result = Solution().isPalindrome(10)
    assert not result
