# https://leetcode.com/problems/leaf-similar-trees

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves: list[int] = []
        leaf_index: int = 0

        def get_leaves(node: TreeNode) -> None:
            nonlocal leaves
            if node:
                if node.left or node.right:
                    if node.left:
                        get_leaves(node.left)
                    if node.right:
                        get_leaves(node.right)
                else:
                    leaves.append(node.val)

        def match_leaves(node: TreeNode) -> bool:
            nonlocal leaves, leaf_index
            result: bool = True
            if node:
                if node.left or node.right:
                    if node.left:
                        result &= match_leaves(node.left)
                    if node.right and result:
                        result &= match_leaves(node.right)
                else:
                    if leaf_index >= len(leaves) or node.val != leaves[leaf_index]:
                        result = False
                    else:
                        leaf_index += 1

            return result

        get_leaves(root1)
        return match_leaves(root2) and leaf_index == len(leaves)
