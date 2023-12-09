# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii


# Provided Node class
class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        level: list[Node] = [root]
        next_level: list[Node] = []

        while len(level) > 0:
            next_level = []

            for index in range(len(level)):
                if level[index].left:
                    next_level.append(level[index].left)
                if level[index].right:
                    next_level.append(level[index].right)
                level[index].next = None if index == len(level) - 1 else level[index + 1]
            level = next_level

        return root
