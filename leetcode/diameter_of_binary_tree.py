# https://leetcode.com/problems/diameter-of-binary-tree/description/

from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter

    def depth(self, node: TreeNode) -> int:
        if node:
            left: int = self.depth(node.left)
            right: int = self.depth(node.right)

            if left + right > self.diameter:
                self.diameter = left + right

            return 1 + max(right, left)
        return 0
