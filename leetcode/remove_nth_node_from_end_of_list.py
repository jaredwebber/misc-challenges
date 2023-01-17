# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional

# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        fast: ListNode = head.next
        slow: ListNode = head

        for i in range(n):
            if fast:
                fast = fast.next
            else:
                return head.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next else None

        return head
