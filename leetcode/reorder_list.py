# https://leetcode.com/problems/reorder-list/description/

from typing import Optional

# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr: ListNode = head
        mid: ListNode = head

        # find midpoint
        prev: ListNode = mid
        while curr and curr.next:
            prev = mid
            mid = mid.next
            curr = curr.next
            if curr.next:
                curr = curr.next
        prev.next = None

        # reverse 2nd half
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        # update alternating pointers
        curr = head
        curr_next = curr.next
        prev_next = prev.next

        if not curr.next and prev != head:
            curr.next = prev
            prev = None

        while curr and prev:
            curr_next = curr.next
            curr.next = prev
            curr = curr_next
            prev_next = prev.next
            prev.next = curr_next
            prev = prev_next

            if curr and prev and curr.next is None:
                curr.next = prev
                break
