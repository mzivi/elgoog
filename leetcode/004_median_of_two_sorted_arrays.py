# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 < l2:  # put longest in nums1
            nums1, nums2, l1, l2 = nums2, nums1, l2, l1
        l = l1 + l2
        if l == 1:
            return nums1[0]
        if l1 == l2 and nums1[0] > nums2[l2-1]:
            return 0.5 * (nums1[0] + nums2[l2-1])
        i = (l1 - 1) // 2
        j = (l + 1) // 2 - i - 2
        min_i = 0
        max_i = l1 - 1
        while True:
            lower1 = nums1[i]  # i always in range as l1 >= l2
            lower2 = nums2[j] if 0 <= j < l2 else lower1
            lower = max(lower1, lower2)
            upper1 = nums1[i+1] if i + 1 < l1 else nums2[j+1]
            upper2 = nums2[j+1] if j + 1 < l2 else upper1
            upper = min(upper1, upper2)
            if lower <= upper:
                break
            if lower1 > lower2 or j < 0:
                max_i = i - 1
                i = max((min_i + i) // 2, (l + 1) // 2 - l2 - 1)
            else:
                min_i = i + 1
                i = min((i + max_i + 1) // 2, (l + 1) // 2 - 1)
            j = (l + 1) // 2 - i - 2
        return 0.5 * (lower + upper) if l % 2 == 0 else lower


if __name__ == '__main__':

    import numpy.testing as testing

    result = Solution().findMedianSortedArrays([1, 6, 7], [2, 3, 4, 5, 8, 9])
    testing.assert_almost_equal(result, 5.0)
    result = Solution().findMedianSortedArrays([1], [2, 3, 4, 5, 6, 7, 8])
    testing.assert_almost_equal(result, 4.5)
    result = Solution().findMedianSortedArrays([5], [1, 2, 3, 4, 6, 7])
    testing.assert_almost_equal(result, 4.0)
    result = Solution().findMedianSortedArrays([1, 3], [2])
    testing.assert_almost_equal(result, 2.0)
    result = Solution().findMedianSortedArrays([1, 2], [3, 4])
    testing.assert_almost_equal(result, 2.5)
    result = Solution().findMedianSortedArrays([], [1])
    testing.assert_almost_equal(result, 1.0)
    result = Solution().findMedianSortedArrays([3], [-2, -1])
    testing.assert_almost_equal(result, -1.0)
    result = Solution().findMedianSortedArrays([2], [])
    testing.assert_almost_equal(result, 2.0)
    result = Solution().findMedianSortedArrays([], [2, 3])
    testing.assert_almost_equal(result, 2.5)
    result = Solution().findMedianSortedArrays([1, 2], [-1, 3])
    testing.assert_almost_equal(result, 1.5)
