# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    result = ''
    for i in range(1, len(s) + 1):
        for j in range(i):
            substr = s[j:i]
            if substr == substr[::-1] and len(substr) > len(result):
                result = substr
    return result


def longestPalindromeDP(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) <= 0:
        return ''

    result = s[0]
    is_pld = [[True]]
    for j in range(1, len(s)):
        row = [True, s[j] == s[j-1]]
        is_pld.append(row)
        if row[-1] and len(result) < 2:
            result = s[j-1:j+1]
        for i in range(j - 2, -1, -1):
            row.append(is_pld[j-1][j-i-2] and s[i] == s[j])
            if row[-1] and j - i + 1 > len(result):
                result = s[i:j + 1]
    return result


def longestPalindromeDP2(s):
    """
    :type s: str
    :rtype: str
    """
    result = ''
    for i in range(len(s)):
        new_result = _expand_from(s, i, i)
        if len(new_result) > len(result):
            result = new_result
        new_result = _expand_from(s, i, i + 1)
        if len(new_result) > len(result):
            result = new_result

    return result


def _expand_from(s, i, j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]


def longestPalindromeDPnew(s):
    if len(s) <= 0:
        return ''

    result = s[0]
    is_pld = [[True, True]]
    for j, cj in enumerate(s[1:]):
        is_pld_j = []
        is_pld_jm1 = is_pld[-1]
        is_pld.append(is_pld_j)
        for i, ci in enumerate(s[:j + 1]):
            is_pld_j.append(is_pld_jm1[i + 1] and ci == cj)
            if is_pld_j[-1] and j - i + 2 > len(result):
                result = s[i:j + 2]
        is_pld_j.append(True)
        is_pld_j.append(True)
    return result


if __name__ == '__main__':
    print(longestPalindrome('babad'))
    print(longestPalindrome('a'))
    print(longestPalindrome('bb'))
    print(longestPalindrome('a' * 10))
    print(longestPalindrome('a' * 1000))
    print('')

    print(longestPalindromeDP('cbbd'))
    print(longestPalindromeDP('babad'))
    print(longestPalindromeDP('bananas'))
    print(longestPalindromeDP('ccc'))
    print('')

    print(longestPalindromeDP2('cbbd'))
    print(longestPalindromeDP2('babad'))
    print(longestPalindromeDP2('bananas'))
    print(longestPalindromeDP2('ccc'))
    print('')

    print(longestPalindromeDPnew('cbbd'))
    print(longestPalindromeDPnew('babad'))
    print(longestPalindromeDPnew('bananas'))
    print(longestPalindromeDPnew('ccc'))
    print('')
