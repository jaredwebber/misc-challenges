# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

from typing import Optional


# Provided ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        values: list[int] = []
        while head:
            values.append(head.val)
            head = head.next

        root: TreeNode = TreeNode()

        def construct(node: TreeNode, left: int, right: int) -> None:
            mid: int = left + ((right - left) // 2)
            node.val = values[mid]

            if right - left > 0:
                if right - left > 1:
                    node.left = TreeNode()
                    construct(node.left, left, mid - 1)
                node.right = TreeNode()
                construct(node.right, mid + 1, right)

        construct(root, 0, len(values) - 1)

        return root
