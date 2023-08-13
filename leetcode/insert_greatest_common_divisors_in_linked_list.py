# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list

from typing import Optional


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr: Optional[ListNode] = head
        while curr and curr.next:
            temp: ListNode = curr.next
            curr.next = ListNode(self.gcd(curr.val, curr.next.val), temp)
            curr = curr.next.next
        return head

    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            temp: int = b
            b = a % b
            a = temp
        return a
