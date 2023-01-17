# https://leetcode.com/problems/binary-tree-level-order-traversal/description

from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        order: list[list[int]] = []
        queue: list[int] = []

        queue.append(root)

        while len(queue) != 0:
            level: list[int] = []
            next_level: list[int] = []
            while len(queue) != 0:
                node: Optional[TreeNode] = queue.pop()
                if node is not None:
                    level.append(node.val)
                    if node.left is not None:
                        next_level.insert(0, node.left)
                    if node.right is not None:
                        next_level.insert(0, node.right)
            if len(level) > 0:
                order.append(level)
            queue.extend(next_level)

        return order
