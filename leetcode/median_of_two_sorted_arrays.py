# https://leetcode.com/problems/median-of-two-sorted-arrays


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined: list[int] = []
        index_one: int = 0
        index_two: int = 0

        while index_one < len(nums1) and index_two < len(nums2):
            if nums1[index_one] <= nums2[index_two]:
                combined.append(nums1[index_one])
                index_one += 1
            else:
                combined.append(nums2[index_two])
                index_two += 1

        if index_one < len(nums1):
            while index_one < len(nums1):
                combined.append(nums1[index_one])
                index_one += 1
        else:
            while index_two < len(nums2):
                combined.append(nums2[index_two])
                index_two += 1

        return (
            combined[(len(combined) // 2)]
            if len(combined) % 2 == 1
            else (combined[(len(combined) // 2)] + combined[(len(combined) // 2) - 1]) / 2
        )
