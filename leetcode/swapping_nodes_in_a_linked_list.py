# https://leetcode.com/problems/swapping-nodes-in-a-linked-list

from typing import Optional


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr: ListNode = head
        count: int = 1
        while curr:
            curr = curr.next
            count += 1

        first: int = min(k, count - k)
        second: int = max(k, count - k)

        if first == second:
            return head

        prev: ListNode = ListNode(next=head)
        curr = prev.next

        for _ in range(first - 1):
            prev = curr
            curr = curr.next

        prev_first: ListNode = prev
        first_node: ListNode = curr
        first_next: ListNode = curr.next

        for _ in range(second - first):
            prev = curr
            curr = curr.next

        prev_second: ListNode = prev
        second_node: ListNode = curr
        second_next: ListNode = curr.next

        prev_first.next = second_node
        if second_node == first_next:
            second_node.next = first_node
        else:
            second_node.next = first_next
        prev_second.next = first_node
        first_node.next = second_next

        return second_node if first == 1 else head
