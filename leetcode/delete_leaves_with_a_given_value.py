# https://leetcode.com/problems/delete-leaves-with-a-given-value

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.delete_nodes(root, target, None, "")
        return root if (root.val != target or root.left or root.right) else None

    def delete_nodes(
        self, node: Optional[TreeNode], target: int, parent: Optional[TreeNode], is_left_child: bool
    ) -> None:
        if node:
            if parent and not node.left and not node.right and node.val == target:
                self.delete(parent, is_left_child)
            else:
                self.delete_nodes(node.left, target, node, True)
                self.delete_nodes(node.right, target, node, False)

                if parent and not node.left and not node.right and node.val == target:
                    self.delete(parent, is_left_child)

    def delete(self, parent: Optional[TreeNode], is_left_child: bool) -> None:
        if is_left_child:
            parent.left = None
        else:
            parent.right = None
