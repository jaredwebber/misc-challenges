# https://leetcode.com/problems/n-ary-tree-postorder-traversal


# Provided Node class
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        order: list[int] = []

        def traverse(node: Node) -> None:
            if node:
                for child in node.children:
                    traverse(child)
                order.append(node.val)

        traverse(root)
        return order
