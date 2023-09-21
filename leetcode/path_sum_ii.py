# https://leetcode.com/problems/path-sum-ii

from typing import Optional
import copy


# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        paths: list[list[int]] = []
        self.traverse(root, 0, targetSum, [], paths)
        return paths

    def traverse(
        self,
        node: Optional[TreeNode],
        curr_sum: int,
        target_sum: int,
        curr_path: list[int],
        paths: list[list[int]],
    ) -> None:
        if node:
            if node.left or node.right:  # not leaf
                orig_path = copy.deepcopy(curr_path)

                curr_path.append(node.val)
                self.traverse(
                    node.left, curr_sum + node.val, target_sum, curr_path, paths
                )

                orig_path.append(node.val)
                self.traverse(
                    node.right, curr_sum + node.val, target_sum, orig_path, paths
                )
            elif curr_sum + node.val == target_sum:  # leaf
                curr_path.append(node.val)
                paths.append(curr_path)
