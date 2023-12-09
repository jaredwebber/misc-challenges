# https://leetcode.com/problems/binary-tree-level-order-traversal-ii

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        result: list[list[int]] = []

        if not root:
            return result

        level: list[TreeNode] = [root]
        next_level: list[TreeNode] = []
        level_vals: list[int] = []
        while len(level) > 0:
            next_level = []
            level_vals = []
            for node in level:
                level_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
            result.insert(0, level_vals)

        return result
