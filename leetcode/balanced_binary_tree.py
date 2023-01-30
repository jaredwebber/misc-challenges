# https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root, 0) != -1

    def balanced(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:  # if None, pass True
            return 1

        left: int = self.balanced(node.left, depth + 1)
        right: int = self.balanced(node.right, depth + 1)
        # abs() check verifies if heights differ by more than 1 and the
        # left and right checks carry the abs() check through the recursion
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1
