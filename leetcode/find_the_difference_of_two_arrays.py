# https://leetcode.com/problems/find-the-difference-of-two-arrays


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return [set(nums1).difference(nums2), set(nums2).difference(nums1)]
