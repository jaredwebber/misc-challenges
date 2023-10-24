# https://leetcode.com/problems/evaluate-boolean-binary-tree

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root)

    def traverse(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return True
        if node.val == 0 or node.val == 1:
            return True if node.val == 1 else False
        if node.val == 2:
            return self.traverse(node.left) or self.traverse(node.right)
        if node.val == 3:
            return self.traverse(node.left) and self.traverse(node.right)
