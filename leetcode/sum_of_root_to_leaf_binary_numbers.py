# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1 if root.val == 1 else 0

        binary_nums: list[str] = []
        self.traverse(root, binary_nums, "")

        total: int = 0
        for i in binary_nums:
            total += int(i, 2)

        return total

    def traverse(self, node: Optional[TreeNode], binary_nums: list[str], curr_val: str):
        if not node.left and not node.right and len(curr_val) > 0:
            binary_nums.append(curr_val + str(node.val))
        else:
            if node.left:
                self.traverse(node.left, binary_nums, curr_val + str(node.val))
            if node.right:
                self.traverse(node.right, binary_nums, curr_val + str(node.val))
