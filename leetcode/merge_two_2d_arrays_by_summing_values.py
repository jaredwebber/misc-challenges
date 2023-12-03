# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values


class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        one: int = 0
        two: int = 0
        merged: list[list[int]] = []

        while one < len(nums1) and two < len(nums2):
            if nums1[one][0] < nums2[two][0]:
                merged.append(nums1[one])
                one += 1
            elif nums1[one][0] > nums2[two][0]:
                merged.append(nums2[two])
                two += 1
            else:
                merged.append([nums2[two][0], nums1[one][1] + nums2[two][1]])
                one += 1
                two += 1

        while one < len(nums1):
            merged.append(nums1[one])
            one += 1
        while two < len(nums2):
            merged.append(nums2[two])
            two += 1

        return merged
