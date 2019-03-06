# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = 0
        result = node = None
        while l1 and l2:
            s = l1.val + l2.val + r
            new_node = ListNode(s % 10)
            r = s // 10
            if node:
                node.next = new_node
                node = new_node
            else:
                result = node = new_node
            l1 = l1.next
            l2 = l2.next
        l = l1 if l1 else l2
        while l:
            s = l.val + r
            new_node = ListNode(s % 10)
            r = s // 10
            if node:
                node.next = new_node
                node = new_node
            else:
                result = node = new_node
            l = l.next
        if r > 0:
            node.next = ListNode(r)
        return result


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8
