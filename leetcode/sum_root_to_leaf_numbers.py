# https://leetcode.com/problems/sum-root-to-leaf-numbers

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers: list[int] = []
        self.traverse(root, "", numbers)
        return sum(numbers)

    def traverse(self, node: Optional[TreeNode], curr: str, numbers: list[int]) -> None:
        if node:
            val: str = str(node.val)
            if not node.left and not node.right:
                numbers.append(int(curr + val))
            else:
                if node.left:
                    self.traverse(node.left, curr + val, numbers)
                if node.right:
                    self.traverse(node.right, curr + val, numbers)
