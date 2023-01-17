# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root, root.val, 0)

    def traverse(self, node: TreeNode, max_parent: int, good_nodes: int) -> int:
        if node:
            if node.val >= max_parent:
                good_nodes += 1
                max_parent = node.val
            return (
                good_nodes
                + self.traverse(node.left, max_parent, 0)
                + self.traverse(node.right, max_parent, 0)
            )

        return good_nodes
