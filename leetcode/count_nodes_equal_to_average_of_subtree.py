# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)[2]

    def traverse(self, node: Optional[TreeNode]) -> (int, int, int):
        if not node.left and not node.right:
            return 1, node.val, 1
        else:
            l_size, l_value, l_hits = self.traverse(node.left) if node.left else (0, 0, 0)
            r_size, r_value, r_hits = self.traverse(node.right) if node.right else (0, 0, 0)
            return (
                l_size + r_size + 1,
                l_value + r_value + node.val,
                l_hits + r_hits + (1 if node.val == (l_value + r_value + node.val) // (l_size + r_size + 1) else 0),
            )
