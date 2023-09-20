# https://leetcode.com/problems/find-largest-value-in-each-tree-row

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        largest: list[int] = []
        self.traverse(root, largest, 0)
        return largest

    def traverse(
        self, node: Optional[TreeNode], largest: list[int], depth: int
    ) -> None:
        if node:
            if len(largest) > depth:
                largest[depth] = max(node.val, largest[depth])
            else:
                largest.append(node.val)
            self.traverse(node.left, largest, depth + 1)
            self.traverse(node.right, largest, depth + 1)
