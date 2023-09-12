# https://leetcode.com/problems/rotate-list


from typing import Optional


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        node_count: int = 0
        curr: ListNode = head
        last: ListNode = None
        while curr is not None:
            node_count += 1
            last = curr
            curr = curr.next

        if k % node_count == 0:
            return head

        prev = head
        curr = head.next
        for i in range(node_count - (k % node_count) - 1):
            prev = curr
            curr = curr.next

        prev.next = None
        last.next = head

        return curr
