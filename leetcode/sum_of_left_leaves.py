# https://leetcode.com/problems/sum-of-left-leaves

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sum_left_leaves(root, False)

    def sum_left_leaves(self, node: Optional[TreeNode], is_left: bool) -> int:
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.val
        return self.sum_left_leaves(node.left, True) + self.sum_left_leaves(node.right, False)
