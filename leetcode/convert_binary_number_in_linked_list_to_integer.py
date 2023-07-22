# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digits: str = ""
        while head is not None:
            digits += str(head.val)
            head = head.next
        return int(digits, 2)
