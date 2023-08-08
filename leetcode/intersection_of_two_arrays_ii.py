# https://leetcode.com/problems/intersection-of-two-arrays-ii


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection: list[int] = []
        nums1.sort()
        nums2.sort()
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] == nums2[0]:
                intersection.append(nums1[0])
                nums1.pop(0)
                nums2.pop(0)
            elif nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)

        return intersection
