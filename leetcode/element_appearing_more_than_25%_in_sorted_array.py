# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        arr.sort()
        curr: int = -1
        count: int = 0

        for i in arr:
            if i == curr:
                count += 1
            else:
                curr = i
                count = 1
            if count > len(arr) / 4:
                return curr

        return -1
