# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        inorder: list[int] = []
        self.traverse(root, inorder)
        return inorder

    def traverse(self, node: Optional[TreeNode], inorder: list[int]) -> None:
        if node:
            self.traverse(node.left, inorder)
            inorder.append(node.val)
            self.traverse(node.right, inorder)
