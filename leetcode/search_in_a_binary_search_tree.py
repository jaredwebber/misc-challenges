# https://leetcode.com/problems/search-in-a-binary-search-tree

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)

    def search(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not node:
            return None
        if node.val == val:
            return node
        if val < node.val:
            return self.search(node.left, val)
        else:
            return self.search(node.right, val)
