# https://leetcode.com/problems/merge-two-binary-trees


from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        combined: TreeNode = TreeNode()
        self.traverse(root1, root2, combined)
        return combined if root1 or root2 else None

    def traverse(self, root1: Optional[TreeNode], root2: Optional[TreeNode], combined: TreeNode) -> None:
        if root1 and root2:
            combined.val = root1.val + root2.val
            if root1.left or root2.left:
                combined.left = TreeNode()
                self.traverse(root1.left, root2.left, combined.left)
            if root1.right or root2.right:
                combined.right = TreeNode()
                self.traverse(root1.right, root2.right, combined.right)
        elif root1:
            combined.val = root1.val
            if root1.left:
                combined.left = TreeNode()
                self.traverse(root1.left, None, combined.left)
            if root1.right:
                combined.right = TreeNode()
                self.traverse(root1.right, None, combined.right)
        elif root2:
            combined.val = root2.val
            if root2.left:
                combined.left = TreeNode()
                self.traverse(None, root2.left, combined.left)
            if root2.right:
                combined.right = TreeNode()
                self.traverse(None, root2.right, combined.right)
