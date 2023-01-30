# https://leetcode.com/problems/path-sum/description/

from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.findPathSum(root, 0, targetSum) if root else False

    def findPathSum(self, node: Optional[TreeNode], currSum: int, target: int) -> bool:
        if node:
            if not node.left and not node.right and currSum + node.val == target:
                return True
            else:
                return self.findPathSum(
                    node.left, currSum + node.val, target
                ) or self.findPathSum(node.right, currSum + node.val, target)
