# https://leetcode.com/problems/invert-binary-tree/description/

# Provided TreeNode class
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root

    def invert(self, node: Optional[TreeNode]) -> None:
        if node is not None:
            temp: Optional[TreeNode] = node.left
            node.left = node.right
            node.right = temp
            self.invert(node.left)
            self.invert(node.right)
