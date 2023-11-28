# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

import sys
from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        top_two: list[int] = [sys.maxsize, sys.maxsize]  # [smallest, second_smallest]

        def traverse(node: Optional[TreeNode]) -> None:
            if node:
                if node.val != top_two[0]:
                    if node.val < top_two[0]:
                        top_two[1] = top_two[0]
                        top_two[0] = node.val
                    elif node.val < top_two[1]:
                        top_two[1] = node.val
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return top_two[1] if top_two[1] != sys.maxsize else -1
