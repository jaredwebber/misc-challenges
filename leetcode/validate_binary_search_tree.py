# https://leetcode.com/problems/validate-binary-search-tree/description/

import sys
from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root.left, -sys.maxsize, root.val) and self.validate(
            root.right, root.val, sys.maxsize
        )

    def validate(self, node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if not node:
            return True

        if node.val > min_val and node.val < max_val:
            return self.validate(node.left, min_val, node.val) and self.validate(
                node.right, node.val, max_val
            )
        return False
