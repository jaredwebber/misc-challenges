# https://leetcode.com/problems/reverse-nodes-in-k-group

from typing import Optional


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_subsection(self, reverse_after: ListNode, reverse_number: int) -> None:
        # ensure enough nodes remain
        temp: ListNode = reverse_after.next
        count: int = 0
        while temp:
            count += 1
            temp = temp.next
            if count > reverse_number:
                break

        if count <= reverse_number:
            return

        # reverse
        prev: ListNode = reverse_after.next
        init_prev = prev
        curr: ListNode = prev.next

        reverse_after.next = None

        for _ in range(reverse_number):
            if not curr:
                return
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        init_prev.next = curr
        reverse_after.next = prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head or not head.next:
            return head

        start: ListNode = ListNode(next=head)
        curr: ListNode = start
        while curr:
            self.reverse_subsection(curr, k - 1)
            for _ in range(k):
                if curr:
                    curr = curr.next
        return start.next
