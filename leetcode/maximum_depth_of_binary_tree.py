# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 1)

    def traverse(self, node: Optional[TreeNode], depth: int) -> int:
        if node is None:
            return depth - 1
        return max(
            self.traverse(node.left, depth + 1), self.traverse(node.right, depth + 1)
        )
