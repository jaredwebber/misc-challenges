# https://leetcode.com/problems/add-two-numbers

from typing import Optional


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one: str = ""
        while l1:
            one += str(l1.val)
            l1 = l1.next

        two: str = ""
        while l2:
            two += str(l2.val)
            l2 = l2.next

        val: str = str(int("".join(reversed(one))) + int("".join(reversed(two))))
        output: ListNode = ListNode()
        curr: ListNode = output

        for i in range(len(val) - 1, -1, -1):
            curr.val = val[i]
            if i > 0:
                temp: ListNode = ListNode()
                curr.next = temp
                curr = temp

        return output
