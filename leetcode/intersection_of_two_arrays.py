# https://leetcode.com/problems/intersection-of-two-arrays


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection: list[int] = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2 and i not in intersection:
                    intersection.append(i)
        else:
            for i in nums2:
                if i in nums1 and i not in intersection:
                    intersection.append(i)
        return intersection
