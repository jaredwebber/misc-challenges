# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total: list[int] = [0]

        def traverse(node: TreeNode) -> None:
            if node:
                traverse(node.right)

                total[0] += node.val
                node.val = total[0]

                traverse(node.left)

        traverse(root)
        return root
