# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

from typing import Optional

# Provided TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        root: Optional[TreeNode] = TreeNode(nums[int(len(nums) / 2)])

        if len(nums) > 1:
            self.build_tree(root, True, nums, 0, int((len(nums) / 2) - 1))
            self.build_tree(root, False, nums, int((len(nums) / 2) + 1), len(nums) - 1)

        return root

    def build_tree(
        self,
        parent: Optional[TreeNode],
        is_left: bool,
        nums: list[int],
        left: int,
        right: int,
    ) -> None:
        if parent and left <= right:
            mid: int = int(left + (right - left) / 2)
            if is_left:
                parent.left = TreeNode(val=nums[mid])
                self.build_tree(parent.left, True, nums, left, mid - 1)
                self.build_tree(parent.left, False, nums, mid + 1, right)
            else:
                parent.right = TreeNode(val=nums[mid])
                self.build_tree(parent.right, True, nums, left, mid - 1)
                self.build_tree(parent.right, False, nums, mid + 1, right)
