# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree

from typing import Optional


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.search_map: dict[int, bool] = {0: True}
        self.recover(root)
        self.root = root

    def recover(self, node: Optional[TreeNode]) -> None:
        if node:
            if node.left:
                node.left.val = 2 * node.val + 1
                self.search_map[node.left.val] = True
                self.recover(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.search_map[node.right.val] = True
                self.recover(node.right)

    def find(self, target: int) -> bool:
        return self.search_map.get(target, False)
