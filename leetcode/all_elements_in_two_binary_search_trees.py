# https://leetcode.com/problems/all-elements-in-two-binary-search-trees


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        elements: list[int] = []

        self.traverse(root1, elements)
        self.traverse(root2, elements)

        elements.sort()
        return elements

    def traverse(self, node: TreeNode, elements: list[int]) -> None:
        if node:
            elements.append(node.val)
            self.traverse(node.left, elements)
            self.traverse(node.right, elements)
