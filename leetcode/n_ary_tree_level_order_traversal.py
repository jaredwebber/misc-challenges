# https://leetcode.com/problems/n-ary-tree-level-order-traversal


# Provided Node class
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:
        if not root:
            return []

        level_order: list[list[int]] = []
        queue: list[Node] = [root]

        next_level: list[Node] = []
        curr_level: list[int] = []
        curr: Node = None

        while len(queue) > 0:
            next_level = []
            curr_level = []

            while len(queue) > 0:
                curr = queue.pop(0)
                for child in curr.children:
                    next_level.append(child)
                curr_level.append(curr.val)

            level_order.append(curr_level)
            queue = next_level

        return level_order
