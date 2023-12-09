# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree
from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        level: list[TreeNode] = [root]
        level_index: int = 0
        next_level: list[TreeNode] = []

        while len(level) > 0:
            next_level = []

            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level_len: int = len(level)
            temp: int = 0
            if level_index % 2 != 0:
                for i in range(level_len // 2):
                    temp = level[i].val
                    level[i].val = level[level_len - 1 - i].val
                    level[level_len - 1 - i].val = temp

            level = next_level
            level_index += 1

        return root
