# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengths = [0]
        prev_len = 0
        hash = {}
        for i in range(len(s)):
            last = s[i]
            j = 1
            while last != s[i - j] and j <= prev_len:
                j += 1
            lengths.append(j)
            prev_len = j
        return max(lengths)

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_max = 0
        hash = {}
        start = 0
        for i, c in enumerate(s):
            if (c not in hash) or (hash[c] < start):
                if i - start + 1 > current_max:
                    current_max = i - start + 1
            else:
                start = hash[c] + 1
            hash[c] = i
        return current_max


if __name__ == '__main__':

    result = Solution().lengthOfLongestSubstring("abcabcbb")
    assert result == 3
    result = Solution().lengthOfLongestSubstring("bbbbb")
    assert result == 1
    result = Solution().lengthOfLongestSubstring("pwwkew")
    assert result == 3
    result = Solution().lengthOfLongestSubstring("")
    assert result == 0

    result = Solution().lengthOfLongestSubstring2("abcabcbb")
    assert result == 3
    result = Solution().lengthOfLongestSubstring2("bbbbb")
    assert result == 1
    result = Solution().lengthOfLongestSubstring2("pwwkew")
    assert result == 3
    result = Solution().lengthOfLongestSubstring2("")
    assert result == 0
