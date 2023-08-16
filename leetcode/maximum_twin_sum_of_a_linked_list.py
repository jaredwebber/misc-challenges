# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

from typing import Optional


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        return self.pairSumArray(head)

    # could also create solution which traverses the list from both ends
    def pairSumArray(self, head: Optional[ListNode]) -> int:
        vals: list[int] = []
        while head is not None:
            vals.append(head.val)
            head = head.next

        maximum: int = 0
        for i in range(0, int(len(vals) / 2)):
            maximum = max(maximum, vals[i] + vals[len(vals) - 1 - i])

        return maximum
