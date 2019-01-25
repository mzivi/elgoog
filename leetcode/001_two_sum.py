# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(1, len(nums)):
        for j in range(i):
            if target == nums[i] + nums[j]:
                return j, i
    raise Exception('No solution found.')


def twoSumHash(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lookup = {}
    for i, v in enumerate(nums):
        if target - v in lookup:
            return lookup[target - v], i
        lookup[v] = i

    raise Exception('No solution found.')


if __name__ == '__main__':

    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
    print(twoSumHash([2, 7, 11, 15], 9))
    print(twoSumHash([3, 2, 4], 6))
