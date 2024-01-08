# https://leetcode.com/problems/range-sum-of-bst


from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum: int = 0

        def traverse(node: TreeNode) -> None:
            nonlocal range_sum
            if node:
                if low <= node.val <= high:
                    range_sum += node.val
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return range_sum
