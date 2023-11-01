# https://leetcode.com/problems/find-mode-in-binary-search-tree

from typing import Optional, List


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        value_ctr: dict[int, int] = {}
        self.traverse(root, value_ctr)

        mode_list: list[int] = []
        common_count: int = 0
        for value, count in value_ctr.items():
            if count == common_count:
                mode_list.append(value)
            elif count > common_count:
                mode_list = [value]
                common_count = count

        return mode_list

    def traverse(self, node: Optional[TreeNode], ctr: dict[int, int]) -> None:
        if node:
            ctr[node.val] = ctr.get(node.val, 0) + 1
            self.traverse(node.left, ctr)
            self.traverse(node.right, ctr)
