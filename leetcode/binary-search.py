# https://leetcode.com/problems/binary-search/description/


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo: int = 0
        hi: int = len(nums) - 1

        while lo <= hi:
            mid: int = int((lo + hi) / 2)
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid

        return -1
