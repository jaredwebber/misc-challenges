# https://leetcode.com/problems/binary-tree-paths

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        paths: list[str] = []
        self.traverse(root, "", paths)
        return paths

    def traverse(self, node: Optional[TreeNode], curr_path: str, paths: list[str]) -> None:
        curr_path += f"->{node.val}" if len(curr_path) > 0 else str(node.val)
        if not node.left and not node.right:
            paths.append(curr_path)
            return
        if node.left:
            self.traverse(node.left, curr_path, paths)
        if node.right:
            self.traverse(node.right, curr_path, paths)
