# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.


class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        p0 = nums[:2]
        p1 = [0, nums[1]]
        m0 = 0
        m1 = 0
        for n in nums[2:-1]:
            m0 = max(m0, p0[-2])
            m1 = max(m1, p1[-2])
            p0.append(n + m0)
            p1.append(n + m1)
        m1 = max(m1, p1[-2])
        p1.append(nums[-1] + m1)
        return max(p0[-2:] + p1[-2:])


if __name__ == "__main__":

    result = Solution().rob([2,7,9,3,1])
    assert result == 11
    result = Solution().rob([2,3,2])
    assert result == 3
    result = Solution().rob([1,2,3,1])
    assert result == 4
