# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.max_diff(root, root.val, root.val, 0)

    def max_diff(self, node: TreeNode, max_ancestor: int, min_ancestor: int, max_diff: int) -> None:
        if node:
            max_diff = max(max_diff, max(abs(max_ancestor - node.val), abs(min_ancestor - node.val)))
            min_ancestor = min(min_ancestor, node.val)
            max_ancestor = max(max_ancestor, node.val)
            return max(
                self.max_diff(node.left, max_ancestor, min_ancestor, max_diff),
                self.max_diff(node.right, max_ancestor, min_ancestor, max_diff),
            )

        return max_diff
