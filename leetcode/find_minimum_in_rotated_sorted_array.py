# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        if len(nums) < 3:
            return min(nums)

        while left < right:
            mid: int = int((left + right) / 2)
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[left]:
                if nums[right] > nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
